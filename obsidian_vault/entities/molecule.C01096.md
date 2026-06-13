---
entity_id: "molecule.C01096"
entity_type: "small_molecule"
name: "Sorbitol 6-phosphate"
source_database: "KEGG"
source_id: "C01096"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Sorbitol 6-phosphate"
  - "D-Sorbitol 6-phosphate"
  - "D-Glucitol 6-phosphate"
---

# Sorbitol 6-phosphate

`molecule.C01096`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01096`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Sorbitol 6-phosphate; D-Sorbitol 6-phosphate; D-Glucitol 6-phosphate EcoCyc common name: D-sorbitol 6-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Sorbitol 6-phosphate; D-Sorbitol 6-phosphate; D-Glucitol 6-phosphate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R05820|reaction.R05820]] `KEGG` `database` - C04261 + C00794 <=> C00615 + C01096
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-169|reaction.ecocyc.TRANS-RXN-169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02866|reaction.R02866]] `KEGG` `database` - C01096 + C00001 <=> C00794 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.SORB6PDEHYDROG-RXN|reaction.ecocyc.SORB6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN|reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01096`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
