---
entity_id: "reaction.ecocyc.TRANS-RXN0-503"
entity_type: "reaction"
name: "TRANS-RXN0-503"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-503"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-503

`reaction.ecocyc.TRANS-RXN0-503`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-503`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MALTOTRIOSE + ATP + WATER -> ADP + Pi + MALTOTRIOSE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MALTOTRIOSE + ATP + WATER -> ADP + Pi + MALTOTRIOSE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltose ABC transporter (complex.ecocyc.ABC-16-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Maltotriose (molecule.C01835). Products: ADP (molecule.C00008), H+ (molecule.C00080), Maltotriose (molecule.C01835), phosphate (molecule.ecocyc.Pi).

## Annotation

MALTOTRIOSE + ATP + WATER -> ADP + Pi + MALTOTRIOSE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-503`

## Notes

MALTOTRIOSE + ATP + WATER -> ADP + Pi + MALTOTRIOSE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
