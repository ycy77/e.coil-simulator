# File and metric snapshot

```json
{
  "project_root": "/home/zkyd/data1/ycy/P_world/coil",
  "file_count": 25355,
  "top_dirs_bytes": {
    "data": 621512632,
    "obsidian_vault": 49798409,
    "logs": 5786919,
    "scripts": 261953,
    "web": 170044,
    "ecoil_sim": 162384,
    "docs": 94388,
    "tests": 27400,
    "configs": 11414,
    "main.py": 9287,
    "README.md": 6649,
    "prompts": 6281,
    "schemas": 3214
  },
  "largest_files": [
    [
      "data/raw/ecocyc/ecoli.tar.gz",
      132883846
    ],
    [
      "data/enriched/entities_enriched_v2.jsonl",
      54566987
    ],
    [
      "data/enriched/entities_enriched.jsonl",
      54566987
    ],
    [
      "data/enriched/_v2/entities_enriched_v2.jsonl",
      54566987
    ],
    [
      "data/registry/native_rules.jsonl",
      36322796
    ],
    [
      "data/enriched/entities_enriched_v2_lite.jsonl",
      25466367
    ],
    [
      "data/enriched/entities_enriched_lite.jsonl",
      25466367
    ],
    [
      "data/enriched/_v2/entities_enriched_v2_lite.jsonl",
      25466367
    ],
    [
      "data/raw/ecocyc/extracted/29.6/data/proteins.dat",
      24351087
    ],
    [
      "data/enriched/entities_enriched_summary.csv",
      13750522
    ],
    [
      "data/normalized/entities.csv",
      13281013
    ],
    [
      "data/normalized/_v2/entities.csv",
      13281013
    ],
    [
      "data/audit/decisions/small_molecule.jsonl",
      12309360
    ],
    [
      "data/normalized/entities.csv.pre_canonical_v2",
      11477956
    ],
    [
      "data/raw/ecocyc/extracted/29.6/data/compounds.dat",
      8747743
    ],
    [
      "data/audit/decisions/protein.jsonl",
      6267691
    ],
    [
      "logs/vllm_gpu6_7.log",
      5784680
    ],
    [
      "data/normalized/ecocyc_entities.csv",
      5540556
    ],
    [
      "data/normalized/edges.csv.pre_canonical_v2",
      5497853
    ],
    [
      "data/normalized/edges.csv",
      5471016
    ]
  ],
  "metrics": {
    "entities_by_type": {
      "small_molecule": 9841,
      "gene": 4506,
      "protein": 4458,
      "reaction": 3874,
      "complex": 1309,
      "rna": 215
    },
    "duplicate_display_names": 0,
    "unique_display_name_ratio": 1.0,
    "edges": 47000,
    "pathways": 615,
    "rules": 47203,
    "audit": {
      "total_decisions": 24319,
      "total_ambiguous": 50,
      "per_type": {
        "gene": {
          "endogenous": 4504,
          "exogenous-drug": 1
        },
        "protein": {
          "endogenous": 4461,
          "exogenous-drug": 8,
          "exogenous-chemical": 10
        },
        "complex": {
          "endogenous": 1340,
          "exogenous-chemical": 3,
          "exogenous-drug": 4
        },
        "reaction": {
          "endogenous": 3833,
          "exogenous-chemical": 56,
          "exogenous-drug": 25
        },
        "small_molecule": {
          "endogenous": 5089,
          "exogenous-chemical": 4285,
          "exogenous-drug": 276,
          "class-abstraction": 209
        },
        "rna": {
          "endogenous": 215
        }
      }
    },
    "canonicalization": {
      "input_entities": 24369,
      "output_entities": 24203,
      "merged_count": 166,
      "orphan_edges_removed": 0,
      "unique_display_name_ratio": 1.0,
      "audit_coverage": 24153
    },
    "enriched_cards": 24203
  }
}
```
