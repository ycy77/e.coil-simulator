---
entity_id: "molecule.C00081"
entity_type: "small_molecule"
name: "ITP"
source_database: "KEGG"
source_id: "C00081"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "ITP"
  - "Inosine 5'-triphosphate"
  - "Inosine triphosphate"
  - "Inosine tripolyphosphate"
---

# ITP

`molecule.C00081`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00081`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: ITP; Inosine 5'-triphosphate; Inosine triphosphate; Inosine tripolyphosphate

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: ITP; Inosine 5'-triphosphate; Inosine triphosphate; Inosine tripolyphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R00722|reaction.R00722]] `KEGG` `database` - C00002 + C00104 <=> C00008 + C00081
- `is_substrate_of` --> [[reaction.R00719|reaction.R00719]] `KEGG` `database` - C00081 + C00001 <=> C00104 + C00009
- `is_substrate_of` --> [[reaction.R00720|reaction.R00720]] `KEGG` `database` - C00081 + C00001 <=> C00130 + C00013
- `is_substrate_of` --> [[reaction.R00724|reaction.R00724]] `KEGG` `database` - C00081 + C00022 <=> C00104 + C00074
- `is_substrate_of` --> [[reaction.R00770|reaction.R00770]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5073|reaction.ecocyc.RXN0-5073]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6382|reaction.ecocyc.RXN0-6382]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00081`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
