---
entity_id: "reaction.ecocyc.AMINEOXID-RXN"
entity_type: "reaction"
name: "Aliphatic-amine oxidase"
source_database: "EcoCyc"
source_id: "AMINEOXID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Aliphatic-amine oxidase

`reaction.ecocyc.AMINEOXID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMINEOXID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction converts an aliphatic amine to an aldehyde. EcoCyc reaction equation: Aliphatic-Amines + WATER + OXYGEN-MOLECULE -> Aldehydes + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction converts an aliphatic amine to an aldehyde.

## Biological Role

Catalyzed by copper-containing amine oxidase (complex.ecocyc.AMINEOXID-CPLX). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), an aliphatic amine (molecule.ecocyc.Aliphatic-Amines). Products: Hydrogen peroxide (molecule.C00027), Aldehyde (molecule.C00071), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

This reaction converts an aliphatic amine to an aldehyde.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.AMINEOXID-CPLX|complex.ecocyc.AMINEOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00071|molecule.C00071]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aliphatic-Amines|molecule.ecocyc.Aliphatic-Amines]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.SEMICARBAZIDE|molecule.ecocyc.SEMICARBAZIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:AMINEOXID-RXN`

## Notes

Aliphatic-Amines + WATER + OXYGEN-MOLECULE -> Aldehydes + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
