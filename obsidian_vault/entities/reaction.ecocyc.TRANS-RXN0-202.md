---
entity_id: "reaction.ecocyc.TRANS-RXN0-202"
entity_type: "reaction"
name: "TRANS-RXN0-202"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-202"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-202

`reaction.ecocyc.TRANS-RXN0-202`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-202`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

WATER + ATP + CPD-218 -> Pi + ADP + CPD-218 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + ATP + CPD-218 -> Pi + ADP + CPD-218 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-methionine/D-methionine ABC transporter (complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), D-Methionine (molecule.C00855). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Methionine (molecule.C00855), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + ATP + CPD-218 -> Pi + ADP + CPD-218 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00855|molecule.C00855]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00855|molecule.C00855]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-202`

## Notes

WATER + ATP + CPD-218 -> Pi + ADP + CPD-218 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
