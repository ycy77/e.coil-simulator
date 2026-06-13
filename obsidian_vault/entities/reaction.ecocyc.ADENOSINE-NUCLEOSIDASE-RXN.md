---
entity_id: "reaction.ecocyc.ADENOSINE-NUCLEOSIDASE-RXN"
entity_type: "reaction"
name: "ADENOSINE-NUCLEOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "ADENOSINE-NUCLEOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENOSINE-NUCLEOSIDASE-RXN

`reaction.ecocyc.ADENOSINE-NUCLEOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENOSINE-NUCLEOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADENOSINE + WATER -> D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ADENOSINE + WATER -> D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rihC (protein.P22564). Substrates: H2O (molecule.C00001), Adenosine (molecule.C00212). Products: Adenine (molecule.C00147), D-ribofuranose (molecule.ecocyc.D-Ribofuranose).

## Enriched Pathways

- `ecocyc.PWY-6605` adenine and adenosine salvage II (EcoCyc)

## Annotation

ADENOSINE + WATER -> D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6605` adenine and adenosine salvage II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P22564|protein.P22564]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ADENOSINE-NUCLEOSIDASE-RXN`

## Notes

ADENOSINE + WATER -> D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT
