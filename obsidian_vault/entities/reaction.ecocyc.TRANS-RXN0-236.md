---
entity_id: "reaction.ecocyc.TRANS-RXN0-236"
entity_type: "reaction"
name: "L-lyxopyranose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-236"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-lyxopyranose:proton symport

`reaction.ecocyc.TRANS-RXN0-236`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-236`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD-15867 -> PROTON + CPD-15867; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CPD-15867 -> PROTON + CPD-15867; direction=REVERSIBLE.

## Biological Role

Catalyzed by rhaT (protein.P27125). Substrates: H+ (molecule.C00080), L-Lyxose (molecule.C01508). Products: H+ (molecule.C00080), L-Lyxose (molecule.C01508).

## Annotation

PROTON + CPD-15867 -> PROTON + CPD-15867; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27125|protein.P27125]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01508|molecule.C01508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01508|molecule.C01508]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-236`

## Notes

PROTON + CPD-15867 -> PROTON + CPD-15867; direction=REVERSIBLE
