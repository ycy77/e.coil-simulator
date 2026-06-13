---
entity_id: "reaction.ecocyc.AMACETOXID-RXN"
entity_type: "reaction"
name: "AMACETOXID-RXN"
source_database: "EcoCyc"
source_id: "AMACETOXID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMACETOXID-RXN

`reaction.ecocyc.AMACETOXID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMACETOXID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This is a specific substrate reaction of the general amine oxidase reaction. EcoCyc reaction equation: AMINO-ACETONE + WATER + OXYGEN-MOLECULE -> METHYL-GLYOXAL + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This is a specific substrate reaction of the general amine oxidase reaction.

## Biological Role

Catalyzed by copper-containing amine oxidase (complex.ecocyc.AMINEOXID-CPLX). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), Aminoacetone (molecule.C01888). Products: Hydrogen peroxide (molecule.C00027), Methylglyoxal (molecule.C00546), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.THRDLCTCAT-PWY` L-threonine degradation III (to methylglyoxal) (EcoCyc)

## Annotation

This is a specific substrate reaction of the general amine oxidase reaction.

## Pathways

- `ecocyc.THRDLCTCAT-PWY` L-threonine degradation III (to methylglyoxal) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.AMINEOXID-CPLX|complex.ecocyc.AMINEOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01888|molecule.C01888]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:AMACETOXID-RXN`

## Notes

AMINO-ACETONE + WATER + OXYGEN-MOLECULE -> METHYL-GLYOXAL + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
