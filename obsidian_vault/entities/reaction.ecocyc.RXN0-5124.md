---
entity_id: "reaction.ecocyc.RXN0-5124"
entity_type: "reaction"
name: "RXN0-5124"
source_database: "EcoCyc"
source_id: "RXN0-5124"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5124

`reaction.ecocyc.RXN0-5124`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5124`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14553 + CPD0-935 -> PROTON + CPD0-936 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14553 + CPD0-935 -> PROTON + CPD0-936 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaB (protein.P27127). Substrates: UDP-alpha-D-galactose (molecule.C00052), glucosyl-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-935). Products: UDP (molecule.C00015), H+ (molecule.C00080), galactosyl-(1→6)-glucosyl-(1→3)-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-936).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

CPD-14553 + CPD0-935 -> PROTON + CPD0-936 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27127|protein.P27127]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-936|molecule.ecocyc.CPD0-936]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00052|molecule.C00052]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-935|molecule.ecocyc.CPD0-935]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5124`

## Notes

CPD-14553 + CPD0-935 -> PROTON + CPD0-936 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
