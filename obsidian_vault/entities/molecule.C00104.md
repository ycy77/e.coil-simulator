---
entity_id: "molecule.C00104"
entity_type: "small_molecule"
name: "IDP"
source_database: "KEGG"
source_id: "C00104"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "IDP"
  - "Inosine 5'-diphosphate"
  - "Inosine diphosphate"
---

# IDP

`molecule.C00104`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00104`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: IDP; Inosine 5'-diphosphate; Inosine diphosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: IDP; Inosine 5'-diphosphate; Inosine diphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00719|reaction.R00719]] `KEGG` `database` - C00081 + C00001 <=> C00104 + C00009
- `is_product_of` --> [[reaction.R00724|reaction.R00724]] `KEGG` `database` - C00081 + C00022 <=> C00104 + C00074
- `is_product_of` --> [[reaction.R00770|reaction.R00770]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354
- `is_product_of` --> [[reaction.ecocyc.RXN0-5073|reaction.ecocyc.RXN0-5073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00722|reaction.R00722]] `KEGG` `database` - C00002 + C00104 <=> C00008 + C00081

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00104`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
