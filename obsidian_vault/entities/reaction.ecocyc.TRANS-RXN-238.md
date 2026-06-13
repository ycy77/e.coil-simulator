---
entity_id: "reaction.ecocyc.TRANS-RXN-238"
entity_type: "reaction"
name: "TRANS-RXN-238"
source_database: "EcoCyc"
source_id: "TRANS-RXN-238"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-238

`reaction.ecocyc.TRANS-RXN-238`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-238`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Aminoalkylphosphonates + ATP + WATER -> Aminoalkylphosphonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Aminoalkylphosphonates + ATP + WATER -> Aminoalkylphosphonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phosphonate/phosphate ABC transporter (complex.ecocyc.ABC-23-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), an (aminoalkyl)phosphonate (molecule.ecocyc.Aminoalkylphosphonates). Products: ADP (molecule.C00008), H+ (molecule.C00080), an (aminoalkyl)phosphonate (molecule.ecocyc.Aminoalkylphosphonates), phosphate (molecule.ecocyc.Pi).

## Annotation

Aminoalkylphosphonates + ATP + WATER -> Aminoalkylphosphonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-23-CPLX|complex.ecocyc.ABC-23-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Aminoalkylphosphonates|molecule.ecocyc.Aminoalkylphosphonates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aminoalkylphosphonates|molecule.ecocyc.Aminoalkylphosphonates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-238`

## Notes

Aminoalkylphosphonates + ATP + WATER -> Aminoalkylphosphonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
