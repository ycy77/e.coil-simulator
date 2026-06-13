---
entity_id: "reaction.ecocyc.KDOTRANS2-RXN"
entity_type: "reaction"
name: "KDOTRANS2-RXN"
source_database: "EcoCyc"
source_id: "KDOTRANS2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDOTRANS2-RXN

`reaction.ecocyc.KDOTRANS2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDOTRANS2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is an essential step in lipopolysaccharide biosynthesis. Two KDO residues are transferred to the lipid A precursor, lipid IVA. This reaction transfers the second residue. EcoCyc reaction equation: KDO-LIPID-IVA + CMP-KDO -> PROTON + KDO2-LIPID-IVA + CMP; direction=PHYSIOL-LEFT-TO-RIGHT. This is an essential step in lipopolysaccharide biosynthesis. Two KDO residues are transferred to the lipid A precursor, lipid IVA. This reaction transfers the second residue.

## Biological Role

Catalyzed by waaA (protein.P0AC75). Substrates: CMP-3-deoxy-D-manno-octulosonate (molecule.C04121), 3-Deoxy-D-manno-octulosonyl-lipid IV(A) (molecule.C06024). Products: CMP (molecule.C00055), H+ (molecule.C00080), KDO2-lipid IVA (molecule.C06025).

## Enriched Pathways

- `ecocyc.KDOSYN-PWY` Kdo transfer to lipid IVA (E. coli) (EcoCyc)

## Annotation

This is an essential step in lipopolysaccharide biosynthesis. Two KDO residues are transferred to the lipid A precursor, lipid IVA. This reaction transfers the second residue.

## Pathways

- `ecocyc.KDOSYN-PWY` Kdo transfer to lipid IVA (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[protein.P0AC75|protein.P0AC75]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04121|molecule.C04121]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06024|molecule.C06024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C04932|molecule.C04932]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06026|molecule.C06026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C21982|molecule.C21982]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1277|molecule.ecocyc.CPD0-1277]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1280|molecule.ecocyc.CPD0-1280]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1283|molecule.ecocyc.CPD0-1283]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1284|molecule.ecocyc.CPD0-1284]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:KDOTRANS2-RXN`

## Notes

KDO-LIPID-IVA + CMP-KDO -> PROTON + KDO2-LIPID-IVA + CMP; direction=PHYSIOL-LEFT-TO-RIGHT
