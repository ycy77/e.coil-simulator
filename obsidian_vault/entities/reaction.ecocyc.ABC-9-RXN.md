---
entity_id: "reaction.ecocyc.ABC-9-RXN"
entity_type: "reaction"
name: "ABC-9-RXN"
source_database: "EcoCyc"
source_id: "ABC-9-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-9-RXN

`reaction.ecocyc.ABC-9-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-9-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + FERRIC-CITRATE-COMPLEX + WATER -> ADP + Pi + FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + FERRIC-CITRATE-COMPLEX + WATER -> ADP + Pi + FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ferric citrate ABC transporter (complex.ecocyc.ABC-9-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Fe(III)dicitrate (molecule.C06229). Products: ADP (molecule.C00008), H+ (molecule.C00080), Fe(III)dicitrate (molecule.C06229), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + FERRIC-CITRATE-COMPLEX + WATER -> ADP + Pi + FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-9-CPLX|complex.ecocyc.ABC-9-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06229|molecule.C06229]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06229|molecule.C06229]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-9-RXN`

## Notes

ATP + FERRIC-CITRATE-COMPLEX + WATER -> ADP + Pi + FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
