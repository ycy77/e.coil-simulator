---
entity_id: "molecule.C00793"
entity_type: "small_molecule"
name: "D-Cysteine"
source_database: "KEGG"
source_id: "C00793"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Cysteine"
  - "D-Amino-3-mercaptopropionic acid"
---

# D-Cysteine

`molecule.C00793`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00793`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Cysteine; D-Amino-3-mercaptopropionic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: D-Cysteine; D-Amino-3-mercaptopropionic acid

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (8)

- `activates` --> [[reaction.ecocyc.TRANS-RXN0-593|reaction.ecocyc.TRANS-RXN0-593]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN-14497|reaction.ecocyc.RXN-14497]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DCYSDESULF-RXN|reaction.ecocyc.DCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19381|reaction.ecocyc.RXN-19381]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6992|reaction.ecocyc.RXN0-6992]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DCYSDESULF-RXN|reaction.ecocyc.DCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00793`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
