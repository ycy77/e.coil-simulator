---
entity_id: "molecule.C11811"
entity_type: "small_molecule"
name: "1-Hydroxy-2-methyl-2-butenyl 4-diphosphate"
source_database: "KEGG"
source_id: "C11811"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1-Hydroxy-2-methyl-2-butenyl 4-diphosphate"
  - "(E)-4-Hydroxy-3-methyl-but-2-enyl diphosphate"
  - "(E)-4-Hydroxy-3-methylbut-2-en-1-yl diphosphate"
---

# 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate

`molecule.C11811`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11811`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate; (E)-4-Hydroxy-3-methyl-but-2-enyl diphosphate; (E)-4-Hydroxy-3-methylbut-2-en-1-yl diphosphate EcoCyc common name: (E)-4-hydroxy-3-methylbut-2-en-1-yl diphosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate; (E)-4-Hydroxy-3-methyl-but-2-enyl diphosphate; (E)-4-Hydroxy-3-methylbut-2-en-1-yl diphosphate

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R08210|reaction.R08210]] `KEGG` `database` - C00235 + 2 C00139 + C00001 <=> C11811 + 2 C00138 + 2 C00080
- `is_product_of` --> [[reaction.ecocyc.RXN-24043|reaction.ecocyc.RXN-24043]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24044|reaction.ecocyc.RXN-24044]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R10859|reaction.R10859]] `KEGG` `database` - C11811 + C00001 + C02869 <=> C11453 + C02745
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15878|reaction.ecocyc.RXN-15878]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11811`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
