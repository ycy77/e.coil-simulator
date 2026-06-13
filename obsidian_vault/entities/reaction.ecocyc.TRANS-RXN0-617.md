---
entity_id: "reaction.ecocyc.TRANS-RXN0-617"
entity_type: "reaction"
name: "TRANS-RXN0-617"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-617"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-617

`reaction.ecocyc.TRANS-RXN0-617`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-617`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

HOMOCYSTINE + ATP + WATER -> HOMOCYSTINE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HOMOCYSTINE + ATP + WATER -> HOMOCYSTINE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cystine ABC transporter (complex.ecocyc.CPLX0-8152). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Homocystine (molecule.C01817). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Homocystine (molecule.C01817), phosphate (molecule.ecocyc.Pi).

## Annotation

HOMOCYSTINE + ATP + WATER -> HOMOCYSTINE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01817|molecule.C01817]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01817|molecule.C01817]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-617`

## Notes

HOMOCYSTINE + ATP + WATER -> HOMOCYSTINE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
