---
entity_id: "molecule.C04896"
entity_type: "small_molecule"
name: "5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide"
source_database: "KEGG"
source_id: "C04896"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide"
  - "N-(5'-Phospho-D-ribosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide"
  - "N-(5'-Phosphoribosylformimino)-5-amino-1-(5''-phosphoribosyl)-4-imidazolecarboxamide"
  - "Phosphoribosyl-formimino-AICAR-phosphate"
  - "1-(5-Phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide"
  - "1-(5-Phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide"
---

# 5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide

`molecule.C04896`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04896`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide; N-(5'-Phospho-D-ribosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide; N-(5'-Phosphoribosylformimino)-5-amino-1-(5''-phosphoribosyl)-4-imidazolecarboxamide; Phosphoribosyl-formimino-AICAR-phosphate; 1-(5-Phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide; 1-(5-Phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide EcoCyc common name: 1-(5-phospho-β-D-ribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: 5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide; N-(5'-Phospho-D-ribosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide; N-(5'-Phosphoribosylformimino)-5-amino-1-(5''-phosphoribosyl)-4-imidazolecarboxamide; Phosphoribosyl-formimino-AICAR-phosphate; 1-(5-Phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide; 1-(5-Phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.HISTCYCLOHYD-RXN|reaction.ecocyc.HISTCYCLOHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04640|reaction.R04640]] `KEGG` `database` - C04896 <=> C04916
- `is_substrate_of` --> [[reaction.ecocyc.PRIBFAICARPISOM-RXN|reaction.ecocyc.PRIBFAICARPISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04896`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
