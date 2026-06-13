---
entity_id: "reaction.ecocyc.PMPOXI-RXN"
entity_type: "reaction"
name: "PMPOXI-RXN"
source_database: "EcoCyc"
source_id: "PMPOXI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PMPOXI-RXN

`reaction.ecocyc.PMPOXI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PMPOXI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the de novo synthesis of pyridoxine and pyridoxal phosphate (PLP). It also functions in the PLP salvage pathway. EcoCyc reaction equation: OXYGEN-MOLECULE + WATER + PYRIDOXAMINE-5P -> AMMONIUM + HYDROGEN-PEROXIDE + PYRIDOXAL_PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the de novo synthesis of pyridoxine and pyridoxal phosphate (PLP). It also functions in the PLP salvage pathway.

## Biological Role

Catalyzed by pyridoxine 5'-phosphate oxidase / pyridoxamine 5'-phosphate oxidase (complex.ecocyc.PDXH-CPLX). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), Pyridoxamine phosphate (molecule.C00647). Products: Pyridoxal phosphate (molecule.C00018), Hydrogen peroxide (molecule.C00027), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Annotation

This reaction is part of the de novo synthesis of pyridoxine and pyridoxal phosphate (PLP). It also functions in the PLP salvage pathway.

## Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.PDXH-CPLX|complex.ecocyc.PDXH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00647|molecule.C00647]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1221|molecule.ecocyc.CPD0-1221]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PMPOXI-RXN`

## Notes

OXYGEN-MOLECULE + WATER + PYRIDOXAMINE-5P -> AMMONIUM + HYDROGEN-PEROXIDE + PYRIDOXAL_PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
