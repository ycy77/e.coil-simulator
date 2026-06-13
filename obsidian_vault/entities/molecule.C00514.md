---
entity_id: "molecule.C00514"
entity_type: "small_molecule"
name: "D-Mannonate"
source_database: "KEGG"
source_id: "C00514"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Mannonate"
---

# D-Mannonate

`molecule.C00514`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00514`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Mannonate

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: D-Mannonate

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MANNONOXIDOREDUCT-RXN|reaction.ecocyc.MANNONOXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN|reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00514`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
