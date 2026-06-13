#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from ecoil_sim.actions import ActionInterpreter
from ecoil_sim.agents import PromptBuilder
from ecoil_sim.config import load_yaml_like
from ecoil_sim.graph import StaticGraph
from ecoil_sim.llm import AsyncVLLMClient, NameResolver, NullLLMClient, RuleBasedMockLLM, load_guided_json
from ecoil_sim.paths import PROJECT_ROOT
from ecoil_sim.registry import RuleRegistry
from ecoil_sim.report import Reporter
from ecoil_sim.report.llm_report_agent import LLMReportAgent
from ecoil_sim.sim.llm_perturbation import VLLMJsonCompleter
from ecoil_sim.retrieval import TemporalGraphRAG
from ecoil_sim.rules import FallbackPolicy
from ecoil_sim.sim.perturbation import NaturalLanguagePerturbationParser
from ecoil_sim.sim.engine import run_sync, SimulationEngine
from ecoil_sim.storage import SimulationStore
from ecoil_sim.state import TemporalState
from ecoil_sim.validation import ActionValidator


def main() -> int:
    parser = argparse.ArgumentParser(description="E.coil molecular agent simulator")
    parser.add_argument("--config", type=Path, default=Path("configs/simulation.yaml"))
    parser.add_argument("--model-config", type=Path, default=Path("configs/model.qwen35_9b.yaml"))
    parser.add_argument("--entity", action="append", default=[], help="Perturbed entity id, can repeat")
    parser.add_argument("--state", default="inhibited", help="State to assign to perturbed entities")
    parser.add_argument("--perturbation", action="append", default=[], help="Natural-language perturbation, can repeat")
    parser.add_argument("--rounds", type=int, default=None)
    parser.add_argument("--initial-profile", type=Path, default=None, help="Initial condition YAML profile")
    parser.add_argument("--resume-run", type=Path, default=None, help="Use a previous run directory as the new round_0 baseline")
    parser.add_argument("--resume-round", type=int, default=None, help="Round number to resume from; defaults to the latest round")
    parser.add_argument("--use-llm", action="store_true")
    parser.add_argument("--llm-report", action="store_true", help="After the run, have a global-view LLM agent write a biological report")
    parser.add_argument("--mock-llm", action="store_true", help="Use deterministic offline mock actions for propagation tests")
    parser.add_argument("--gpus", type=int, default=None, help="GPU count used to calculate agent/concurrency budget")
    parser.add_argument("--agents-per-gpu", type=int, default=None, help="Active-agent budget per GPU")
    parser.add_argument("--max-active-agents", type=int, default=None)
    args = parser.parse_args()

    config = load_yaml_like(PROJECT_ROOT / args.config)
    model_config = load_yaml_like(PROJECT_ROOT / args.model_config)
    graph_cfg = config.get("graph", {})
    sim_cfg = config.get("simulation", {})
    resource_cfg = config.get("resources", {})
    llm_run_cfg = config.get("llm", {})
    gpu_count = args.gpus or int(resource_cfg.get("default_gpus", 1))
    agents_per_gpu = args.agents_per_gpu or int(resource_cfg.get("agents_per_gpu", 50))
    max_active_agents = args.max_active_agents or (gpu_count * agents_per_gpu)

    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / graph_cfg.get("normalized_dir", "data/normalized"))
    registry = RuleRegistry.from_registry_dir(PROJECT_ROOT / graph_cfg.get("registry_dir", "data/registry"))
    edge_cfg = load_yaml_like(PROJECT_ROOT / graph_cfg.get("edge_weights", "configs/edge_weights.yaml"))
    retriever = TemporalGraphRAG(
        graph=graph,
        registry=registry,
        edge_weights=edge_cfg.get("edge_weights", {}),
        state_distance=edge_cfg.get("state_distance", {}),
        min_score=float(sim_cfg.get("min_retrieval_score", 0.2)),
    )
    prompt_builder = PromptBuilder(PROJECT_ROOT / "prompts/agent_decision.system.md")
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    store_root = PROJECT_ROOT / sim_cfg.get("store_root", "runs") / run_id
    store = SimulationStore(store_root)
    initial_profile = {}
    initial_state = None
    run_context = {}
    if args.resume_run:
        resume_run = _project_path(args.resume_run)
        snapshot_path = _resume_snapshot_path(resume_run, args.resume_round)
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
        initial_state = TemporalState.from_snapshot(
            graph.entities.values(),
            snapshot=snapshot,
            source_run=str(resume_run),
        )
        run_context = {
            "start_mode": "resume_run",
            "resume_run": str(resume_run),
            "resume_round": snapshot.get("round"),
        }
    else:
        initial_profile_path = args.initial_profile or Path(
            sim_cfg.get("initial_profile", "data/initial_conditions/glucose_log_phase.yaml")
        )
        initial_profile_abs = _project_path(initial_profile_path)
        if initial_profile_abs.exists():
            initial_profile = load_yaml_like(initial_profile_abs)
            run_context = {
                "start_mode": "initial_profile",
                "initial_profile": str(initial_profile_abs),
                "profile_id": initial_profile.get("profile_id", ""),
            }
        else:
            run_context = {
                "start_mode": "entity_defaults",
                "initial_profile_missing": str(initial_profile_abs),
            }

    if args.mock_llm:
        llm_client = RuleBasedMockLLM()
    elif args.use_llm:
        llm_cfg = model_config.get("llm", {})
        llm_client = AsyncVLLMClient(
            base_url=llm_cfg.get("base_url", "http://localhost:8000/v1"),
            api_key=llm_cfg.get("api_key", "EMPTY"),
            model=llm_cfg.get("model", ""),
            max_concurrency=gpu_count * int(llm_run_cfg.get("max_concurrency_per_gpu", agents_per_gpu)),
            timeout_seconds=float(llm_run_cfg.get("timeout_seconds", 120)),
            max_retries=int(llm_run_cfg.get("max_retries", 2)),
            max_tokens=int(llm_cfg.get("decision_max_tokens", 256)),
            temperature=float(llm_cfg.get("temperature", 0.2)),
            top_p=float(llm_cfg.get("top_p", 0.8)),
            guided_json=load_guided_json(model_config, PROJECT_ROOT),
            enable_thinking=bool(llm_cfg.get("enable_thinking", False)),
        )
    else:
        llm_client = NullLLMClient()

    perturbations = [
        {
            "entity_id": entity_id,
            "state": args.state,
            "source": "database",
            "input_source": "cli",
            "reason": "CLI perturbation",
        }
        for entity_id in args.entity
    ]
    perturb_cfg = config.get("perturbation", {})
    knowledge_path = PROJECT_ROOT / perturb_cfg.get("knowledge_base", "data/perturbations/perturbation_knowledge.yaml")
    parser_nl = NaturalLanguagePerturbationParser(graph, knowledge_path=knowledge_path)
    unresolved = []
    for text in args.perturbation:
        parsed = parser_nl.parse(text)
        perturbations.extend(parsed.changes)
        unresolved.extend(parsed.unresolved)

    fallback_path = PROJECT_ROOT / config.get("fallback", {}).get("policy", "configs/fallback_rules.yaml")
    fallback_policy = FallbackPolicy.from_config(fallback_path)
    name_resolver = NameResolver(graph.entities.values())
    validator = ActionValidator(name_resolver=name_resolver)
    action_interpreter = ActionInterpreter(graph, fallback_policy=fallback_policy)
    engine = SimulationEngine(
        graph=graph,
        registry=registry,
        retriever=retriever,
        prompt_builder=prompt_builder,
        store=store,
        llm_client=llm_client,
        name_resolver=name_resolver,
        action_interpreter=action_interpreter,
        validator=validator,
    )
    state = run_sync(
        engine,
        perturbations=perturbations,
        max_rounds=args.rounds if args.rounds is not None else int(sim_cfg.get("max_rounds", 5)),
        max_active_agents=max_active_agents,
        steady_state_patience=int(
            sim_cfg.get("steady_state_patience", sim_cfg.get("convergence_patience", 2))
        ),
        initial_state=initial_state,
        initial_profile=initial_profile,
        run_context=run_context,
    )
    phenotype_db = PROJECT_ROOT / config.get("report", {}).get("phenotype_db", "data/phenotypes/phenotype_db.yaml")
    reporter = Reporter(graph=graph, phenotype_db=phenotype_db, name_resolver=name_resolver)
    report = reporter.summarize_changes(state)
    narrative = reporter.render_narrative(report)
    print(f"run_store={store_root}")
    print(f"resource_budget={{'gpus': {gpu_count}, 'agents_per_gpu': {agents_per_gpu}, 'max_active_agents': {max_active_agents}}}")
    if unresolved:
        print(f"unresolved_perturbations={unresolved}")
    print(narrative)
    if args.llm_report:
        llm_cfg = model_config.get("llm", {})
        completer = VLLMJsonCompleter(
            base_url=llm_cfg.get("base_url", "http://localhost:8000/v1"),
            model=llm_cfg.get("model", ""),
            api_key=llm_cfg.get("api_key", "EMPTY"),
            max_tokens=int(llm_cfg.get("default_max_tokens", 1024)),
        )
        report_agent = LLMReportAgent(
            completer, graph=graph, prompt_path=PROJECT_ROOT / "prompts/report_agent.system.md"
        )
        try:
            print("\n===== LLM biological report (global view) =====")
            print(report_agent.write_report(report))
        except Exception as exc:  # never let the report agent crash a finished run
            print(f"[llm-report] skipped: {exc}")
    print(f"structured_report={report}")
    return 0


def _project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def _resume_snapshot_path(run_dir: Path, round_number: int | None = None) -> Path:
    rounds_dir = run_dir / "rounds"
    if round_number is not None:
        path = rounds_dir / f"round_{round_number}.json"
        if not path.exists():
            raise FileNotFoundError(f"resume round not found: {path}")
        return path
    candidates = sorted(
        rounds_dir.glob("round_*.json"),
        key=lambda item: int(item.stem.split("_")[-1]),
    )
    if not candidates:
        raise FileNotFoundError(f"no round snapshots found in {rounds_dir}")
    return candidates[-1]


if __name__ == "__main__":
    raise SystemExit(main())
