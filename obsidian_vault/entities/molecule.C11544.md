---
entity_id: "molecule.C11544"
entity_type: "small_molecule"
name: "2-O-(alpha-D-Mannosyl)-D-glycerate"
source_database: "KEGG"
source_id: "C11544"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-O-(alpha-D-Mannosyl)-D-glycerate"
  - "alpha-Mannosylglycerate"
  - "2-O-(alpha-D-Mannopyranosyl)-D-glycerate"
---

# 2-O-(alpha-D-Mannosyl)-D-glycerate

`molecule.C11544`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11544`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-O-(alpha-D-Mannosyl)-D-glycerate; alpha-Mannosylglycerate; 2-O-(alpha-D-Mannopyranosyl)-D-glycerate EcoCyc common name: 2-O-(α-D-mannosyl)-D-glycerate. 2-O-ALPHA-MANNOSYL-D-GLYCERATE is a major compatible solute in halophilic or halotolerant thermophilic bacteria .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: 2-O-(alpha-D-Mannosyl)-D-glycerate; alpha-Mannosylglycerate; 2-O-(alpha-D-Mannopyranosyl)-D-glycerate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R05790|reaction.R05790]] `KEGG` `database` - C11516 + C00001 <=> C11544 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2522|reaction.ecocyc.RXN0-2522]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11544`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
