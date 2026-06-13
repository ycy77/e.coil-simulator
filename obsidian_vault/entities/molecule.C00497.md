---
entity_id: "molecule.C00497"
entity_type: "small_molecule"
name: "(R)-Malate"
source_database: "KEGG"
source_id: "C00497"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-Malate"
  - "D-Malate"
  - "D-Malic acid"
---

# (R)-Malate

`molecule.C00497`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00497`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-Malate; D-Malate; D-Malic acid

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Annotation

KEGG compound: (R)-Malate; D-Malate; D-Malic acid

## Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-451|reaction.ecocyc.TRANS-RXN0-451]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00215|reaction.R00215]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.83-RXN|reaction.ecocyc.1.1.1.83-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23715|reaction.ecocyc.RXN-23715]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-451|reaction.ecocyc.TRANS-RXN0-451]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ASPARTASE-RXN|reaction.ecocyc.ASPARTASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-703|reaction.ecocyc.RXN0-703]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00497`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
