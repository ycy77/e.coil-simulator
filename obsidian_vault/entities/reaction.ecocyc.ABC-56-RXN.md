---
entity_id: "reaction.ecocyc.ABC-56-RXN"
entity_type: "reaction"
name: "ABC-56-RXN"
source_database: "EcoCyc"
source_id: "ABC-56-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-56-RXN

`reaction.ecocyc.ABC-56-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-56-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + Aliphatic-Sulfonates + WATER -> Aliphatic-Sulfonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + Aliphatic-Sulfonates + WATER -> Aliphatic-Sulfonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aliphatic sulfonate ABC transporter (complex.ecocyc.ABC-56-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), an aliphatic sulfonate (molecule.ecocyc.Aliphatic-Sulfonates). Products: ADP (molecule.C00008), H+ (molecule.C00080), an aliphatic sulfonate (molecule.ecocyc.Aliphatic-Sulfonates), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + Aliphatic-Sulfonates + WATER -> Aliphatic-Sulfonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-56-CPLX|complex.ecocyc.ABC-56-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Aliphatic-Sulfonates|molecule.ecocyc.Aliphatic-Sulfonates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aliphatic-Sulfonates|molecule.ecocyc.Aliphatic-Sulfonates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-56-RXN`

## Notes

ATP + Aliphatic-Sulfonates + WATER -> Aliphatic-Sulfonates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
