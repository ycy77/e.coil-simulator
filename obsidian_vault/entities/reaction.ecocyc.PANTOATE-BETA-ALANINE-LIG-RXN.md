---
entity_id: "reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN"
entity_type: "reaction"
name: "PANTOATE-BETA-ALANINE-LIG-RXN"
source_database: "EcoCyc"
source_id: "PANTOATE-BETA-ALANINE-LIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PANTOATE-BETA-ALANINE-LIG-RXN

`reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PANTOATE-BETA-ALANINE-LIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in pantothenate biosynthesis. EcoCyc reaction equation: B-ALANINE + L-PANTOATE + ATP -> PROTON + PANTOTHENATE + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third step in pantothenate biosynthesis.

## Biological Role

Catalyzed by pantothenate synthetase (complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX). Substrates: ATP (molecule.C00002), beta-Alanine (molecule.C00099), (R)-Pantoate (molecule.C00522). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), Pantothenate (molecule.C00864).

## Enriched Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Annotation

This is the third step in pantothenate biosynthesis.

## Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX|complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00864|molecule.C00864]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00099|molecule.C00099]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00522|molecule.C00522]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1141|molecule.ecocyc.CPD0-1141]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PANTOATE-BETA-ALANINE-LIG-RXN`

## Notes

B-ALANINE + L-PANTOATE + ATP -> PROTON + PANTOTHENATE + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
