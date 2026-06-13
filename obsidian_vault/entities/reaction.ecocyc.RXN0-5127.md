---
entity_id: "reaction.ecocyc.RXN0-5127"
entity_type: "reaction"
name: "RXN0-5127"
source_database: "EcoCyc"
source_id: "RXN0-5127"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5127

`reaction.ecocyc.RXN0-5127`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5127`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-938 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD-21359 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-938 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD-21359 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaU (protein.P27242). Substrates: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398), galactosyl-(glucosyl)3-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-938). Products: ADP (molecule.C00008), H+ (molecule.C00080), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

CPD0-938 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD-21359 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27242|protein.P27242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-938|molecule.ecocyc.CPD0-938]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5127`

## Notes

CPD0-938 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD-21359 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
