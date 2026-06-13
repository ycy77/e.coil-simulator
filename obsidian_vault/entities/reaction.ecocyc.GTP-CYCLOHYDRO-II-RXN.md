---
entity_id: "reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN"
entity_type: "reaction"
name: "GTP-CYCLOHYDRO-II-RXN"
source_database: "EcoCyc"
source_id: "GTP-CYCLOHYDRO-II-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GTP-CYCLOHYDRO-II-RXN

`reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GTP-CYCLOHYDRO-II-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first reaction in the synthesis of riboflavin. EcoCyc reaction equation: WATER + GTP -> PROTON + Pi + DIAMINO-OH-PHOSPHORIBOSYLAMINO-PYR + FORMATE; direction=PHYSIOL-LEFT-TO-RIGHT. The first reaction in the synthesis of riboflavin.

## Biological Role

Catalyzed by GTP cyclohydrolase 2 (complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Formate (molecule.C00058), H+ (molecule.C00080), 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one (molecule.C01304), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

The first reaction in the synthesis of riboflavin.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX|complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01304|molecule.C01304]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00700|molecule.C00700]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.GUANOSINE_TETRAPHOSPHATE|molecule.ecocyc.GUANOSINE_TETRAPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GTP-CYCLOHYDRO-II-RXN`

## Notes

WATER + GTP -> PROTON + Pi + DIAMINO-OH-PHOSPHORIBOSYLAMINO-PYR + FORMATE; direction=PHYSIOL-LEFT-TO-RIGHT
