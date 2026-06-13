---
entity_id: "reaction.ecocyc.ABC-18-RXN"
entity_type: "reaction"
name: "ABC-18-RXN"
source_database: "EcoCyc"
source_id: "ABC-18-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-18-RXN

`reaction.ecocyc.ABC-18-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-18-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + D-galactopyranose + WATER -> ADP + Pi + D-galactopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + D-galactopyranose + WATER -> ADP + Pi + D-galactopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by D-galactose / methyl-β-D-galactoside ABC transporter (complex.ecocyc.ABC-18-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), D-Galactose (molecule.C00124). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Galactose (molecule.C00124), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + D-galactopyranose + WATER -> ADP + Pi + D-galactopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-18-CPLX|complex.ecocyc.ABC-18-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-18-RXN`

## Notes

ATP + D-galactopyranose + WATER -> ADP + Pi + D-galactopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
