---
entity_id: "reaction.ecocyc.KDOTRANS-RXN"
entity_type: "reaction"
name: "KDOTRANS-RXN"
source_database: "EcoCyc"
source_id: "KDOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDOTRANS-RXN

`reaction.ecocyc.KDOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is an essential step in lipopolysaccharide biosynthesis. Two KDO residues are transferred to the lipid A precursor, lipid IVA. This reaction transfers the first residue. EcoCyc reaction equation: CMP-KDO + LIPID-IV-A -> PROTON + KDO-LIPID-IVA + CMP; direction=PHYSIOL-LEFT-TO-RIGHT. This is an essential step in lipopolysaccharide biosynthesis. Two KDO residues are transferred to the lipid A precursor, lipid IVA. This reaction transfers the first residue.

## Biological Role

Catalyzed by waaA (protein.P0AC75). Substrates: CMP-3-deoxy-D-manno-octulosonate (molecule.C04121), 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate (molecule.C04919). Products: CMP (molecule.C00055), H+ (molecule.C00080), 3-Deoxy-D-manno-octulosonyl-lipid IV(A) (molecule.C06024).

## Enriched Pathways

- `ecocyc.KDOSYN-PWY` Kdo transfer to lipid IVA (E. coli) (EcoCyc)

## Annotation

This is an essential step in lipopolysaccharide biosynthesis. Two KDO residues are transferred to the lipid A precursor, lipid IVA. This reaction transfers the first residue.

## Pathways

- `ecocyc.KDOSYN-PWY` Kdo transfer to lipid IVA (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[protein.P0AC75|protein.P0AC75]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06024|molecule.C06024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04121|molecule.C04121]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04919|molecule.C04919]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C04932|molecule.C04932]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06026|molecule.C06026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C21982|molecule.C21982]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1277|molecule.ecocyc.CPD0-1277]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1283|molecule.ecocyc.CPD0-1283]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1284|molecule.ecocyc.CPD0-1284]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:KDOTRANS-RXN`

## Notes

CMP-KDO + LIPID-IV-A -> PROTON + KDO-LIPID-IVA + CMP; direction=PHYSIOL-LEFT-TO-RIGHT
