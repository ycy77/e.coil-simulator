---
entity_id: "reaction.ecocyc.RXN-9597"
entity_type: "reaction"
name: "RXN-9597"
source_database: "EcoCyc"
source_id: "RXN-9597"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Diamine oxidase"
  - "DAO"
  - "Diamino oxhydrase"
  - "Histaminase"
---

# RXN-9597

`reaction.ecocyc.RXN-9597`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9597`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Primary-Amines + WATER + OXYGEN-MOLECULE + PROTON -> Aldehydes + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Primary-Amines + WATER + OXYGEN-MOLECULE + PROTON -> Aldehydes + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by copper-containing amine oxidase (complex.ecocyc.AMINEOXID-CPLX). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), H+ (molecule.C00080), a primary amine (molecule.ecocyc.Primary-Amines). Products: Hydrogen peroxide (molecule.C00027), Aldehyde (molecule.C00071), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

Primary-Amines + WATER + OXYGEN-MOLECULE + PROTON -> Aldehydes + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.AMINEOXID-CPLX|complex.ecocyc.AMINEOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00071|molecule.C00071]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Primary-Amines|molecule.ecocyc.Primary-Amines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9597`

## Notes

Primary-Amines + WATER + OXYGEN-MOLECULE + PROTON -> Aldehydes + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
