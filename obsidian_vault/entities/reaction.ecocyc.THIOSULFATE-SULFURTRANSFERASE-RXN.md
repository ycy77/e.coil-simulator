---
entity_id: "reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN"
entity_type: "reaction"
name: "THIOSULFATE-SULFURTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "THIOSULFATE-SULFURTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "THIOSULFATE THIOTRANSFERASE"
  - "THIOSULFATE CYANIDE TRANSSULFURASE"
  - "RHODANESE"
---

# THIOSULFATE-SULFURTRANSFERASE-RXN

`reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THIOSULFATE-SULFURTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

A FEW OTHER SULFUR COMPOUNDS CAN ACT AS DONORS. EcoCyc reaction equation: S2O3 + HCN -> HSCN + SO3 + PROTON; direction=LEFT-TO-RIGHT. A FEW OTHER SULFUR COMPOUNDS CAN ACT AS DONORS.

## Biological Role

Catalyzed by thiosulfate sulfurtransferase GlpE (complex.ecocyc.CPLX0-242), thiosulfate sulfurtransferase YgaP (complex.ecocyc.CPLX0-8219), pspE (protein.P23857), sseA (protein.P31142). Substrates: Thiosulfate (molecule.C00320), Hydrogen cyanide (molecule.C01326). Products: H+ (molecule.C00080), Sulfite (molecule.C00094), thiocyanate (molecule.ecocyc.HSCN).

## Enriched Pathways

- `ecocyc.PWY-5350` thiosulfate disproportionation IV (rhodanese) (EcoCyc)

## Annotation

A FEW OTHER SULFUR COMPOUNDS CAN ACT AS DONORS.

## Pathways

- `ecocyc.PWY-5350` thiosulfate disproportionation IV (rhodanese) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-242|complex.ecocyc.CPLX0-242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8219|complex.ecocyc.CPLX0-8219]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P23857|protein.P23857]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P31142|protein.P31142]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.HSCN|molecule.ecocyc.HSCN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THIOSULFATE-SULFURTRANSFERASE-RXN`

## Notes

S2O3 + HCN -> HSCN + SO3 + PROTON; direction=LEFT-TO-RIGHT
