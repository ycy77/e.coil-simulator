---
entity_id: "reaction.ecocyc.TRANS-RXN-141A"
entity_type: "reaction"
name: "TRANS-RXN-141A"
source_database: "EcoCyc"
source_id: "TRANS-RXN-141A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-141A

`reaction.ecocyc.TRANS-RXN-141A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-141A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CO+2 -> CO+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CO+2 -> CO+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by divalent metal ion transporter ZupT (complex.ecocyc.CPLX0-8617), corA (protein.P0ABI4). Substrates: Cobalt ion (molecule.C00175). Products: Cobalt ion (molecule.C00175).

## Annotation

CO+2 -> CO+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8617|complex.ecocyc.CPLX0-8617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABI4|protein.P0ABI4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-10715|molecule.ecocyc.CPD-10715]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-141A`

## Notes

CO+2 -> CO+2; direction=LEFT-TO-RIGHT
