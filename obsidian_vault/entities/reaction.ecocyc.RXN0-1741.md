---
entity_id: "reaction.ecocyc.RXN0-1741"
entity_type: "reaction"
name: "RXN0-1741"
source_database: "EcoCyc"
source_id: "RXN0-1741"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1741

`reaction.ecocyc.RXN0-1741`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1741`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltose outer membrane channel / phage lambda receptor protein (complex.ecocyc.CPLX0-7655). Substrates: Maltose (molecule.C00208). Products: Maltose (molecule.C00208).

## Annotation

MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7655|complex.ecocyc.CPLX0-7655]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1741`

## Notes

MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT
