---
entity_id: "reaction.ecocyc.RXN-8638"
entity_type: "reaction"
name: "RXN-8638"
source_database: "EcoCyc"
source_id: "RXN-8638"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8638

`reaction.ecocyc.RXN-8638`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8638`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Quaternary-Amines + WATER + ATP -> Quaternary-Amines + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Quaternary-Amines + WATER + ATP -> Quaternary-Amines + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glycine betaine ABC transporter (complex.ecocyc.ABC-26-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), a quaternary ammonium compound (molecule.ecocyc.Quaternary-Amines). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi), a quaternary ammonium compound (molecule.ecocyc.Quaternary-Amines).

## Annotation

Quaternary-Amines + WATER + ATP -> Quaternary-Amines + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-26-CPLX|complex.ecocyc.ABC-26-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Quaternary-Amines|molecule.ecocyc.Quaternary-Amines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Quaternary-Amines|molecule.ecocyc.Quaternary-Amines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8638`

## Notes

Quaternary-Amines + WATER + ATP -> Quaternary-Amines + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
