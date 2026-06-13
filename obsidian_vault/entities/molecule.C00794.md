---
entity_id: "molecule.C00794"
entity_type: "small_molecule"
name: "D-Sorbitol"
source_database: "KEGG"
source_id: "C00794"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Sorbitol"
  - "D-Glucitol"
  - "L-Gulitol"
  - "Sorbitol"
---

# D-Sorbitol

`molecule.C00794`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00794`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Sorbitol; D-Glucitol; L-Gulitol; Sorbitol

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Sorbitol; D-Glucitol; L-Gulitol; Sorbitol

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.MONOMER-56|complex.ecocyc.MONOMER-56]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R02866|reaction.R02866]] `KEGG` `database` - C01096 + C00001 <=> C00794 + C00009
- `is_product_of` --> [[reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN|reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05820|reaction.R05820]] `KEGG` `database` - C04261 + C00794 <=> C00615 + C01096
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-278|reaction.ecocyc.RXN0-278]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-169|reaction.ecocyc.TRANS-RXN-169]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN-156|reaction.ecocyc.TRANS-RXN-156]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00794`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
