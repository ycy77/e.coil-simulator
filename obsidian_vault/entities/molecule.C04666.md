---
entity_id: "molecule.C04666"
entity_type: "small_molecule"
name: "D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate"
source_database: "KEGG"
source_id: "C04666"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate"
  - "D-erythro-Imidazole-glycerol 3-phosphate"
  - "D-erythro-Imidazole-glycerol phosphate"
---

# D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate

`molecule.C04666`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04666`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate; D-erythro-Imidazole-glycerol 3-phosphate; D-erythro-Imidazole-glycerol phosphate EcoCyc common name: D-erythro-1-(imidazol-4-yl)-glycerol 3-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate; D-erythro-Imidazole-glycerol 3-phosphate; D-erythro-Imidazole-glycerol phosphate

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R12152|reaction.R12152]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001
- `is_product_of` --> [[reaction.ecocyc.GLUTAMIDOTRANS-RXN|reaction.ecocyc.GLUTAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17900|reaction.ecocyc.RXN-17900]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03457|reaction.R03457]] `KEGG` `database` - C04666 <=> C01267 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.IMIDPHOSDEHYD-RXN|reaction.ecocyc.IMIDPHOSDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04666`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
