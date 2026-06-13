---
entity_id: "reaction.ecocyc.RXN-16938"
entity_type: "reaction"
name: "RXN-16938"
source_database: "EcoCyc"
source_id: "RXN-16938"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC-CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16938

`reaction.ecocyc.RXN-16938`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16938`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC-CCO-PERI-BAC

## Enriched Summary

This reaction hydrolyzes the amide bond linking N-acetylmuramyl acid and L-alanine residues. EcoCyc reaction equation: CPD0-2283 + WATER -> CPD-18259 + CPD0-1085; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction hydrolyzes the amide bond linking N-acetylmuramyl acid and L-alanine residues.

## Biological Role

Catalyzed by amiB (protein.P26365), amiA (protein.P36548), amiC (protein.P63883). Substrates: H2O (molecule.C00001), peptidoglycan dimer with pentapeptide stems (meso-diaminopimelate containing) (molecule.ecocyc.CPD0-2283). Products: peptidoglycan dimer with a single pentapeptide stem (meso-diaminopimelate containing) (molecule.ecocyc.CPD-18259), L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine (molecule.ecocyc.CPD0-1085).

## Annotation

This reaction hydrolyzes the amide bond linking N-acetylmuramyl acid and L-alanine residues.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0ADA3|protein.P0ADA3]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P37690|protein.P37690]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.Q46798|protein.Q46798]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P26365|protein.P26365]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P36548|protein.P36548]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P63883|protein.P63883]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18259|molecule.ecocyc.CPD-18259]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1085|molecule.ecocyc.CPD0-1085]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2283|molecule.ecocyc.CPD0-2283]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16938`

## Notes

CPD0-2283 + WATER -> CPD-18259 + CPD0-1085; direction=PHYSIOL-LEFT-TO-RIGHT
