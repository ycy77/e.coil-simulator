---
entity_id: "reaction.ecocyc.TRANS-RXN-290"
entity_type: "reaction"
name: "TRANS-RXN-290"
source_database: "EcoCyc"
source_id: "TRANS-RXN-290"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-290

`reaction.ecocyc.TRANS-RXN-290`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-290`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1564 + ATP + WATER -> CPD0-1564 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1564 + ATP + WATER -> CPD0-1564 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cystine ABC transporter (complex.ecocyc.CPLX0-8152). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), D-cystine (molecule.ecocyc.CPD0-1564). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-cystine (molecule.ecocyc.CPD0-1564), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD0-1564 + ATP + WATER -> CPD0-1564 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-290`

## Notes

CPD0-1564 + ATP + WATER -> CPD0-1564 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
