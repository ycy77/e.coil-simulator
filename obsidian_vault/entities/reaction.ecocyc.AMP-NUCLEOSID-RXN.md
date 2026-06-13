---
entity_id: "reaction.ecocyc.AMP-NUCLEOSID-RXN"
entity_type: "reaction"
name: "AMP-NUCLEOSID-RXN"
source_database: "EcoCyc"
source_id: "AMP-NUCLEOSID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMP-NUCLEOSID-RXN

`reaction.ecocyc.AMP-NUCLEOSID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMP-NUCLEOSID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction regulates AMP concentrations through the hydrolysis of the N-glycosidic bond of AMP. EcoCyc reaction equation: WATER + AMP -> CPD-15317 + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction regulates AMP concentrations through the hydrolysis of the N-glycosidic bond of AMP.

## Biological Role

Catalyzed by AMP nucleosidase (complex.ecocyc.AMP-NUCLEOSID-CPLX), nucleotide 5'-monophosphate nucleosidase (complex.ecocyc.CPLX0-8262). Substrates: H2O (molecule.C00001), AMP (molecule.C00020). Products: Adenine (molecule.C00147), D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317).

## Enriched Pathways

- `ecocyc.PWY-6617` adenosine nucleotides degradation III (EcoCyc)

## Annotation

This reaction regulates AMP concentrations through the hydrolysis of the N-glycosidic bond of AMP.

## Pathways

- `ecocyc.PWY-6617` adenosine nucleotides degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.CPD0-1634|molecule.ecocyc.CPD0-1634]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.AMP-NUCLEOSID-CPLX|complex.ecocyc.AMP-NUCLEOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8262|complex.ecocyc.CPLX0-8262]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1635|molecule.ecocyc.CPD0-1635]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:AMP-NUCLEOSID-RXN`

## Notes

WATER + AMP -> CPD-15317 + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT
