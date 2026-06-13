---
entity_id: "reaction.ecocyc.TRANS-RXN-297"
entity_type: "reaction"
name: "TRANS-RXN-297"
source_database: "EcoCyc"
source_id: "TRANS-RXN-297"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-297

`reaction.ecocyc.TRANS-RXN-297`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-297`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-621 + ATP + WATER -> CPD0-621 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-621 + ATP + WATER -> CPD0-621 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by Fe(3+) hydroxamate ABC transporter (complex.ecocyc.ABC-11-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), iron(III)-coprogen (molecule.ecocyc.CPD0-621). Products: ADP (molecule.C00008), H+ (molecule.C00080), iron(III)-coprogen (molecule.ecocyc.CPD0-621), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD0-621 + ATP + WATER -> CPD0-621 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-11-CPLX|complex.ecocyc.ABC-11-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-621|molecule.ecocyc.CPD0-621]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-621|molecule.ecocyc.CPD0-621]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-297`

## Notes

CPD0-621 + ATP + WATER -> CPD0-621 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
