---
entity_id: "reaction.ecocyc.TRANS-RXN0-510"
entity_type: "reaction"
name: "TRANS-RXN0-510"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-510

`reaction.ecocyc.TRANS-RXN0-510`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-510`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-3738 + WATER + ATP -> CPD-3738 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3738 + WATER + ATP -> CPD-3738 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-methionine/D-methionine ABC transporter (complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), N-acetyl-DL-methionine (molecule.ecocyc.CPD-3738). Products: ADP (molecule.C00008), H+ (molecule.C00080), N-acetyl-DL-methionine (molecule.ecocyc.CPD-3738), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-3738 + WATER + ATP -> CPD-3738 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3738|molecule.ecocyc.CPD-3738]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3738|molecule.ecocyc.CPD-3738]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-510`

## Notes

CPD-3738 + WATER + ATP -> CPD-3738 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
