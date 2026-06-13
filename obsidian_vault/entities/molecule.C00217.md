---
entity_id: "molecule.C00217"
entity_type: "small_molecule"
name: "D-Glutamate"
source_database: "KEGG"
source_id: "C00217"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glutamate"
  - "D-Glutamic acid"
  - "D-Glutaminic acid"
  - "D-2-Aminoglutaric acid"
---

# D-Glutamate

`molecule.C00217`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00217`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glutamate; D-Glutamic acid; D-Glutaminic acid; D-2-Aminoglutaric acid

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: D-Glutamate; D-Glutamic acid; D-Glutaminic acid; D-2-Aminoglutaric acid

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00260|reaction.R00260]] `KEGG` `database` - C00025 <=> C00217
- `is_product_of` --> [[reaction.ecocyc.GLUTRACE-RXN|reaction.ecocyc.GLUTRACE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN|reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTDEHYD-RXN|reaction.ecocyc.GLUTDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00217`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
