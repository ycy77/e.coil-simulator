---
entity_id: "reaction.ecocyc.TRANS-RXN-236"
entity_type: "reaction"
name: "TRANS-RXN-236"
source_database: "EcoCyc"
source_id: "TRANS-RXN-236"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-236

`reaction.ecocyc.TRANS-RXN-236`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-236`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

LOS + ATP + WATER -> LOS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LOS + ATP + WATER -> LOS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ATP-dependent Lipid A-core flippase (complex.ecocyc.CPLX0-7704). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), a lipid A-core oligosaccharide (molecule.ecocyc.LOS). Products: ADP (molecule.C00008), H+ (molecule.C00080), a lipid A-core oligosaccharide (molecule.ecocyc.LOS), phosphate (molecule.ecocyc.Pi).

## Annotation

LOS + ATP + WATER -> LOS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7704|complex.ecocyc.CPLX0-7704]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.LOS|molecule.ecocyc.LOS]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.LOS|molecule.ecocyc.LOS]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-4584|molecule.ecocyc.CPD-4584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1229|molecule.ecocyc.CPD0-1229]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1230|molecule.ecocyc.CPD0-1230]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-236`

## Notes

LOS + ATP + WATER -> LOS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
