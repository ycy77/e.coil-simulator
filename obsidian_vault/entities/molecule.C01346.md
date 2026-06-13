---
entity_id: "molecule.C01346"
entity_type: "small_molecule"
name: "dUDP"
source_database: "KEGG"
source_id: "C01346"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dUDP"
  - "2'-Deoxyuridine 5'-diphosphate"
---

# dUDP

`molecule.C01346`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01346`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dUDP; 2'-Deoxyuridine 5'-diphosphate

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: dUDP; 2'-Deoxyuridine 5'-diphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (5)

- `is_substrate_of` --> [[reaction.R02331|reaction.R02331]] `KEGG` `database` - C00002 + C01346 <=> C00008 + C00460
- `is_substrate_of` --> [[reaction.ecocyc.DUDPKIN-RXN|reaction.ecocyc.DUDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-722|reaction.ecocyc.RXN0-722]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPREDUCT-RXN|reaction.ecocyc.UDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DUTP-PYROP-RXN|reaction.ecocyc.DUTP-PYROP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01346`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
