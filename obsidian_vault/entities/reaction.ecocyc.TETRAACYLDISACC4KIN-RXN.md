---
entity_id: "reaction.ecocyc.TETRAACYLDISACC4KIN-RXN"
entity_type: "reaction"
name: "TETRAACYLDISACC4KIN-RXN"
source_database: "EcoCyc"
source_id: "TETRAACYLDISACC4KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TETRAACYLDISACC4KIN-RXN

`reaction.ecocyc.TETRAACYLDISACC4KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TETRAACYLDISACC4KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction yields the lipid A precursor, lipid IV(A). EcoCyc reaction equation: BISOHMYR-GLC + ATP -> PROTON + LIPID-IV-A + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction yields the lipid A precursor, lipid IV(A).

## Biological Role

Catalyzed by lpxK (protein.P27300). Substrates: ATP (molecule.C00002), Lipid A disaccharide (molecule.C04932). Products: ADP (molecule.C00008), H+ (molecule.C00080), 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate (molecule.C04919).

## Enriched Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Annotation

This reaction yields the lipid A precursor, lipid IV(A).

## Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P27300|protein.P27300]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04919|molecule.C04919]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04932|molecule.C04932]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TETRAACYLDISACC4KIN-RXN`

## Notes

BISOHMYR-GLC + ATP -> PROTON + LIPID-IV-A + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
