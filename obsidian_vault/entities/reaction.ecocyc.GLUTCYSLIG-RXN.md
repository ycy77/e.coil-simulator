---
entity_id: "reaction.ecocyc.GLUTCYSLIG-RXN"
entity_type: "reaction"
name: "GLUTCYSLIG-RXN"
source_database: "EcoCyc"
source_id: "GLUTCYSLIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTCYSLIG-RXN

`reaction.ecocyc.GLUTCYSLIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTCYSLIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in glutathione biosynthesis. EcoCyc reaction equation: CYS + GLT + ATP -> PROTON + L-GAMMA-GLUTAMYLCYSTEINE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in glutathione biosynthesis.

## Biological Role

Catalyzed by putative glutamate—cysteine ligase 2 (complex.ecocyc.CPLX0-7827), gshA (protein.P0A6W9). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), L-Cysteine (molecule.C00097). Products: ADP (molecule.C00008), H+ (molecule.C00080), gamma-L-Glutamyl-L-cysteine (molecule.C00669), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.GLUTATHIONESYN-PWY` glutathione biosynthesis (EcoCyc)

## Annotation

This is the first reaction in glutathione biosynthesis.

## Pathways

- `ecocyc.GLUTATHIONESYN-PWY` glutathione biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7827|complex.ecocyc.CPLX0-7827]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A6W9|protein.P0A6W9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00669|molecule.C00669]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BUTHIONINE-SULFOXIMINE|molecule.ecocyc.BUTHIONINE-SULFOXIMINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTCYSLIG-RXN`

## Notes

CYS + GLT + ATP -> PROTON + L-GAMMA-GLUTAMYLCYSTEINE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
