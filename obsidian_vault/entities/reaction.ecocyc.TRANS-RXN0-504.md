---
entity_id: "reaction.ecocyc.TRANS-RXN0-504"
entity_type: "reaction"
name: "TRANS-RXN0-504"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-504"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-504

`reaction.ecocyc.TRANS-RXN0-504`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-504`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MALTOTETRAOSE + ATP + WATER -> ADP + MALTOTETRAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MALTOTETRAOSE + ATP + WATER -> ADP + MALTOTETRAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltose ABC transporter (complex.ecocyc.ABC-16-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), maltotetraose (molecule.ecocyc.MALTOTETRAOSE). Products: ADP (molecule.C00008), H+ (molecule.C00080), maltotetraose (molecule.ecocyc.MALTOTETRAOSE), phosphate (molecule.ecocyc.Pi).

## Annotation

MALTOTETRAOSE + ATP + WATER -> ADP + MALTOTETRAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-504`

## Notes

MALTOTETRAOSE + ATP + WATER -> ADP + MALTOTETRAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
