---
entity_id: "reaction.ecocyc.RXN-10817"
entity_type: "reaction"
name: "phenylethylamine oxidase"
source_database: "EcoCyc"
source_id: "RXN-10817"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# phenylethylamine oxidase

`reaction.ecocyc.RXN-10817`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10817`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This is a specific substrate reaction of the general amine oxidase reaction. This reaction is involved in the catabolism of 2-phenylethylamine. EcoCyc reaction equation: WATER + OXYGEN-MOLECULE + PHENYLETHYLAMINE -> PHENYLACETALDEHYDE + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This is a specific substrate reaction of the general amine oxidase reaction. This reaction is involved in the catabolism of 2-phenylethylamine.

## Biological Role

Catalyzed by copper-containing amine oxidase (complex.ecocyc.AMINEOXID-CPLX). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), Phenethylamine (molecule.C05332). Products: Hydrogen peroxide (molecule.C00027), Phenylacetaldehyde (molecule.C00601), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.2PHENDEG-PWY` phenylethylamine degradation I (EcoCyc)

## Annotation

This is a specific substrate reaction of the general amine oxidase reaction. This reaction is involved in the catabolism of 2-phenylethylamine.

## Pathways

- `ecocyc.2PHENDEG-PWY` phenylethylamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.AMINEOXID-CPLX|complex.ecocyc.AMINEOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00601|molecule.C00601]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05332|molecule.C05332]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13895|molecule.ecocyc.CPD-13895]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13898|molecule.ecocyc.CPD-13898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7656|molecule.ecocyc.CPD-7656]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IPRONIAZID|molecule.ecocyc.IPRONIAZID]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.ISONIAZIDE|molecule.ecocyc.ISONIAZIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SEMICARBAZIDE|molecule.ecocyc.SEMICARBAZIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-10817`

## Notes

WATER + OXYGEN-MOLECULE + PHENYLETHYLAMINE -> PHENYLACETALDEHYDE + AMMONIUM + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
