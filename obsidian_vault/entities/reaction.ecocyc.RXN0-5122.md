---
entity_id: "reaction.ecocyc.RXN0-5122"
entity_type: "reaction"
name: "RXN0-5122"
source_database: "EcoCyc"
source_id: "RXN0-5122"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5122

`reaction.ecocyc.RXN0-5122`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5122`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-933 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-934 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-933 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-934 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaQ (protein.P25742). Substrates: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398), glucosyl-(heptosyl)2-Kdo2-lipid A-phosphate (molecule.ecocyc.CPD0-933). Products: ADP (molecule.C00008), H+ (molecule.C00080), glucosyl-(heptosyl)3-Kdo2-lipid A-phosphate (E. coli) (molecule.ecocyc.CPD0-934).

## Annotation

CPD0-933 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-934 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25742|protein.P25742]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-934|molecule.ecocyc.CPD0-934]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-933|molecule.ecocyc.CPD0-933]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5122`

## Notes

CPD0-933 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-934 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
