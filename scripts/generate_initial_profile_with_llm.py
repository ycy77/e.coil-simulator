#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.config import load_yaml_like
from ecoil_sim.graph import StaticGraph


SYSTEM_PROMPT = """You annotate initial discrete states for E. coli MG1655 molecular agents.
Use only the provided entity IDs and allowed states.
Do not invent entities, pathways, concentrations, or biological rules.
Return strict JSON:
{
  "overrides": {
    "<entity_id>": {
      "state": "<allowed state>",
      "abundance_label": "<absent|low|medium|high or empty>",
      "confidence": "<high|medium|low>",
      "reason": "<short reason>"
    }
  }
}
Only include entities whose initial state should differ from the default baseline.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an initial-condition profile draft with an LLM")
    parser.add_argument("--condition", default="glucose logarithmic aerobic growth")
    parser.add_argument("--output", type=Path, default=Path("data/initial_conditions/generated/glucose_log_phase.llm_draft.yaml"))
    parser.add_argument("--config", type=Path, default=Path("configs/simulation.yaml"))
    parser.add_argument("--model-config", type=Path, default=Path("configs/model.qwen35_9b.yaml"))
    parser.add_argument("--entity-type", action="append", default=[], help="Filter entity type; can repeat")
    parser.add_argument("--query", action="append", default=[], help="Search query for candidate entities; can repeat")
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--use-llm", action="store_true", help="Actually call the configured OpenAI-compatible vLLM server")
    parser.add_argument("--max-concurrency", type=int, default=8)
    args = parser.parse_args()

    graph_cfg = load_yaml_like(PROJECT_ROOT / args.config).get("graph", {})
    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / graph_cfg.get("normalized_dir", "data/normalized"))
    entities = select_entities(graph, args.entity_type, args.query, args.limit)
    batches = [entities[index:index + args.batch_size] for index in range(0, len(entities), args.batch_size)]
    messages = [build_messages(args.condition, batch) for batch in batches]

    output = args.output if args.output.is_absolute() else PROJECT_ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    if not args.use_llm:
        prompt_path = output.with_suffix(".prompts.json")
        prompt_path.write_text(json.dumps(messages, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        draft = base_profile(args.condition, source="llm_inference", review_status="dry_run_prompts_only")
        draft["candidate_entities"] = len(entities)
        draft["prompt_file"] = str(prompt_path)
        write_yaml_like(output, draft)
        print(f"dry_run_profile={output}")
        print(f"prompt_file={prompt_path}")
        print(f"candidate_entities={len(entities)} batches={len(batches)}")
        return 0

    model_cfg = load_yaml_like(PROJECT_ROOT / args.model_config).get("llm", {})
    overrides = asyncio.run(call_llm_batches(model_cfg, messages, args.max_concurrency))
    validated = validate_overrides(graph, overrides)
    draft = base_profile(args.condition, source="llm_inference", review_status="unreviewed")
    draft["overrides"] = validated
    draft["candidate_entities"] = len(entities)
    write_yaml_like(output, draft)
    print(f"draft_profile={output}")
    print(f"candidate_entities={len(entities)} overrides={len(validated)}")
    return 0


def select_entities(graph: StaticGraph, entity_types: List[str], queries: List[str], limit: int):
    selected = {}
    if queries:
        for query in queries:
            for entity in graph.search_entities(query, limit=limit):
                if entity_types and entity.entity_type not in set(entity_types):
                    continue
                selected[entity.entity_id] = entity
    else:
        for entity in graph.entities.values():
            if entity_types and entity.entity_type not in set(entity_types):
                continue
            selected[entity.entity_id] = entity
            if len(selected) >= limit:
                break
    return list(selected.values())[:limit]


def build_messages(condition: str, entities) -> List[Dict[str, str]]:
    payload = {
        "condition": condition,
        "entities": [
            {
                "entity_id": entity.entity_id,
                "entity_type": entity.entity_type,
                "name": entity.name,
                "aliases": entity.aliases[:8],
                "default_state": entity.default_state,
                "allowed_states": entity.allowed_states,
                "annotation": entity.annotation[:900],
                "pathways": entity.pathways[:500],
            }
            for entity in entities
        ],
    }
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
    ]


async def call_llm_batches(model_cfg: Dict[str, Any], messages_list: List[List[Dict[str, str]]], max_concurrency: int):
    import httpx

    semaphore = asyncio.Semaphore(max_concurrency)
    async with httpx.AsyncClient(timeout=120) as client:
        tasks = [call_one(client, semaphore, model_cfg, messages) for messages in messages_list]
        results = await asyncio.gather(*tasks)
    merged = {}
    for result in results:
        merged.update(result.get("overrides", {}) if isinstance(result, dict) else {})
    return merged


async def call_one(client, semaphore, model_cfg: Dict[str, Any], messages: List[Dict[str, str]]) -> Dict[str, Any]:
    async with semaphore:
        payload = {
            "model": model_cfg.get("model", ""),
            "messages": messages,
            "temperature": float(model_cfg.get("temperature", 0.2)),
            "top_p": float(model_cfg.get("top_p", 0.8)),
            "max_tokens": int(model_cfg.get("default_max_tokens", 512)),
            "extra_body": {
                "chat_template_kwargs": {"enable_thinking": False},
                "enable_thinking": False,
            },
        }
        headers = {
            "Authorization": f"Bearer {model_cfg.get('api_key', 'EMPTY')}",
            "Content-Type": "application/json",
        }
        response = await client.post(f"{model_cfg.get('base_url', 'http://localhost:8000/v1').rstrip('/')}/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        text = response.json().get("choices", [{}])[0].get("message", {}).get("content") or ""
        match = re.search(r"\{[\s\S]*\}", text)
        if not match:
            return {"overrides": {}}
        try:
            parsed = json.loads(match.group(0))
        except json.JSONDecodeError:
            return {"overrides": {}}
        return parsed if isinstance(parsed, dict) else {"overrides": {}}


def validate_overrides(graph: StaticGraph, overrides: Dict[str, Any]) -> Dict[str, Any]:
    valid = {}
    for entity_id, spec in overrides.items():
        entity = graph.entities.get(entity_id)
        if not entity or not isinstance(spec, dict):
            continue
        state = spec.get("state", "")
        abundance = spec.get("abundance_label", "")
        if state and state not in entity.allowed_states:
            continue
        if abundance and abundance not in {"absent", "low", "medium", "high"}:
            continue
        confidence = spec.get("confidence", "low")
        if confidence not in {"high", "medium", "low"}:
            confidence = "low"
        valid[entity_id] = {
            "state": state or entity.default_state,
            "abundance_label": abundance,
            "confidence": confidence,
            "reason": spec.get("reason", "LLM initial-condition annotation draft"),
        }
    return valid


def base_profile(condition: str, source: str, review_status: str) -> Dict[str, Any]:
    return {
        "profile_id": slug(condition),
        "description": f"LLM-generated draft initial condition for: {condition}",
        "source": source,
        "confidence": "low",
        "review_status": review_status,
        "overrides": {},
    }


def slug(text: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", text.strip().lower()).strip("_")
    return value or "initial_condition"


def write_yaml_like(path: Path, data: Dict[str, Any]) -> None:
    try:
        import yaml  # type: ignore
    except ImportError:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
