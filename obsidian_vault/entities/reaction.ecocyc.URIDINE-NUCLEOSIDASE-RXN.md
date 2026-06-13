---
entity_id: "reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN"
entity_type: "reaction"
name: "URIDINE-NUCLEOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "URIDINE-NUCLEOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URIDINE-NUCLEOSIDASE-RXN

`reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URIDINE-NUCLEOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

URIDINE + WATER -> D-Ribofuranose + URACIL; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: URIDINE + WATER -> D-Ribofuranose + URACIL; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyrimidine-specific ribonucleoside hydrolase RihB (complex.ecocyc.CPLX0-7904), pyrimidine-specific ribonucleoside hydrolase RihA (complex.ecocyc.CPLX0-8280), rihC (protein.P22564). Substrates: H2O (molecule.C00001), Uridine (molecule.C00299). Products: Uracil (molecule.C00106), D-ribofuranose (molecule.ecocyc.D-Ribofuranose).

## Enriched Pathways

- `ecocyc.PWY-6556` pyrimidine ribonucleosides salvage II (EcoCyc)

## Annotation

URIDINE + WATER -> D-Ribofuranose + URACIL; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6556` pyrimidine ribonucleosides salvage II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7904|complex.ecocyc.CPLX0-7904]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8280|complex.ecocyc.CPLX0-8280]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P22564|protein.P22564]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:URIDINE-NUCLEOSIDASE-RXN`

## Notes

URIDINE + WATER -> D-Ribofuranose + URACIL; direction=PHYSIOL-LEFT-TO-RIGHT
