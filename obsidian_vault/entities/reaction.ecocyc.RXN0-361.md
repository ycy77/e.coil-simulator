---
entity_id: "reaction.ecocyc.RXN0-361"
entity_type: "reaction"
name: "RXN0-361"
source_database: "EcoCyc"
source_id: "RXN0-361"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-361

`reaction.ecocyc.RXN0-361`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-361`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYTIDINE + WATER -> D-Ribofuranose + CYTOSINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYTIDINE + WATER -> D-Ribofuranose + CYTOSINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyrimidine-specific ribonucleoside hydrolase RihB (complex.ecocyc.CPLX0-7904), pyrimidine-specific ribonucleoside hydrolase RihA (complex.ecocyc.CPLX0-8280), rihC (protein.P22564). Substrates: H2O (molecule.C00001), Cytidine (molecule.C00475). Products: Cytosine (molecule.C00380), D-ribofuranose (molecule.ecocyc.D-Ribofuranose).

## Enriched Pathways

- `ecocyc.PWY-7195` pyrimidine ribonucleosides salvage III (EcoCyc)

## Annotation

CYTIDINE + WATER -> D-Ribofuranose + CYTOSINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7195` pyrimidine ribonucleosides salvage III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7904|complex.ecocyc.CPLX0-7904]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8280|complex.ecocyc.CPLX0-8280]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P22564|protein.P22564]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00380|molecule.C00380]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-361`

## Notes

CYTIDINE + WATER -> D-Ribofuranose + CYTOSINE; direction=PHYSIOL-LEFT-TO-RIGHT
