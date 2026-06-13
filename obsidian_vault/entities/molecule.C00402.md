---
entity_id: "molecule.C00402"
entity_type: "small_molecule"
name: "D-Aspartate"
source_database: "KEGG"
source_id: "C00402"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Aspartate"
  - "D-Aspartic acid"
---

# D-Aspartate

`molecule.C00402`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00402`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Aspartate; D-Aspartic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: D-Aspartate; D-Aspartic acid

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-19728|reaction.ecocyc.RXN-19728]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23928|reaction.ecocyc.RXN-23928]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23929|reaction.ecocyc.RXN-23929]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00402`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
