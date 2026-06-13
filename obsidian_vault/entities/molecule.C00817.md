---
entity_id: "molecule.C00817"
entity_type: "small_molecule"
name: "D-Altronate"
source_database: "KEGG"
source_id: "C00817"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Altronate"
---

# D-Altronate

`molecule.C00817`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00817`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Altronate

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: D-Altronate

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (4)

- `activates` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_substrate_of` --> [[reaction.R01540|reaction.R01540]] `KEGG` `database` - C00817 <=> C00204 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN|reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALTRODEHYDRAT-RXN|reaction.ecocyc.ALTRODEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00817`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
