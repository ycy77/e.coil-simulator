---
entity_id: "molecule.C00663"
entity_type: "small_molecule"
name: "beta-D-Glucose 1-phosphate"
source_database: "KEGG"
source_id: "C00663"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "beta-D-Glucose 1-phosphate"
---

# beta-D-Glucose 1-phosphate

`molecule.C00663`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00663`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: beta-D-Glucose 1-phosphate EcoCyc common name: β-D-glucopyranose 1-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

KEGG compound: beta-D-Glucose 1-phosphate

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R07264|reaction.R07264]] `KEGG` `database` - C15548 + C00009 <=> C00031 + C00663
- `is_product_of` --> [[reaction.ecocyc.2.4.1.230-RXN|reaction.ecocyc.2.4.1.230-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN|reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16995|reaction.ecocyc.RXN-16995]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00663`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
