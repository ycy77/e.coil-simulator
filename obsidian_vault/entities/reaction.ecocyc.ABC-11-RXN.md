---
entity_id: "reaction.ecocyc.ABC-11-RXN"
entity_type: "reaction"
name: "ABC-11-RXN"
source_database: "EcoCyc"
source_id: "ABC-11-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-11-RXN

`reaction.ecocyc.ABC-11-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-11-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + Ferric-Hydroxamate-Complexes + WATER -> ADP + Pi + Ferric-Hydroxamate-Complexes + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + Ferric-Hydroxamate-Complexes + WATER -> ADP + Pi + Ferric-Hydroxamate-Complexes + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by Fe(3+) hydroxamate ABC transporter (complex.ecocyc.ABC-11-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), a ferric hydroxamate complex (molecule.ecocyc.Ferric-Hydroxamate-Complexes). Products: ADP (molecule.C00008), H+ (molecule.C00080), a ferric hydroxamate complex (molecule.ecocyc.Ferric-Hydroxamate-Complexes), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + Ferric-Hydroxamate-Complexes + WATER -> ADP + Pi + Ferric-Hydroxamate-Complexes + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-11-CPLX|complex.ecocyc.ABC-11-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ferric-Hydroxamate-Complexes|molecule.ecocyc.Ferric-Hydroxamate-Complexes]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ferric-Hydroxamate-Complexes|molecule.ecocyc.Ferric-Hydroxamate-Complexes]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-11-RXN`

## Notes

ATP + Ferric-Hydroxamate-Complexes + WATER -> ADP + Pi + Ferric-Hydroxamate-Complexes + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
