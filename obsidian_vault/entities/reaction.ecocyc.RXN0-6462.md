---
entity_id: "reaction.ecocyc.RXN0-6462"
entity_type: "reaction"
name: "RXN0-6462"
source_database: "EcoCyc"
source_id: "RXN0-6462"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6462

`reaction.ecocyc.RXN0-6462`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6462`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + CPLX0-8288 -> MONOMER0-4178 + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPLX0-8288 -> MONOMER0-4178 + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1512` CusSR Two-Component Signal Transduction System (EcoCyc)

## Annotation

ATP + CPLX0-8288 -> MONOMER0-4178 + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1512` CusSR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `activates` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6462`

## Notes

ATP + CPLX0-8288 -> MONOMER0-4178 + ADP; direction=LEFT-TO-RIGHT
