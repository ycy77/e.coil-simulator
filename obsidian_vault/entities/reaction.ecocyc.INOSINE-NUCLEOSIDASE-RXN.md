---
entity_id: "reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN"
entity_type: "reaction"
name: "INOSINE-NUCLEOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "INOSINE-NUCLEOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# INOSINE-NUCLEOSIDASE-RXN

`reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:INOSINE-NUCLEOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

INOSINE + WATER -> D-Ribofuranose + HYPOXANTHINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: INOSINE + WATER -> D-Ribofuranose + HYPOXANTHINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rihC (protein.P22564). Substrates: H2O (molecule.C00001), Inosine (molecule.C00294). Products: Hypoxanthine (molecule.C00262), D-ribofuranose (molecule.ecocyc.D-Ribofuranose).

## Annotation

INOSINE + WATER -> D-Ribofuranose + HYPOXANTHINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P22564|protein.P22564]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:INOSINE-NUCLEOSIDASE-RXN`

## Notes

INOSINE + WATER -> D-Ribofuranose + HYPOXANTHINE; direction=PHYSIOL-LEFT-TO-RIGHT
