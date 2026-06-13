---
entity_id: "reaction.ecocyc.RXN0-5125"
entity_type: "reaction"
name: "RXN0-5125"
source_database: "EcoCyc"
source_id: "RXN0-5125"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5125

`reaction.ecocyc.RXN0-5125`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5125`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12575 + CPD0-936 -> PROTON + CPD0-937 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12575 + CPD0-936 -> PROTON + CPD0-937 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaO (protein.P27128). Substrates: UDP-glucose (molecule.C00029), galactosyl-(1→6)-glucosyl-(1→3)-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-936). Products: UDP (molecule.C00015), H+ (molecule.C00080), galactosyl-(glucosyl)2-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-937).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

CPD-12575 + CPD0-936 -> PROTON + CPD0-937 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27128|protein.P27128]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-937|molecule.ecocyc.CPD0-937]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-936|molecule.ecocyc.CPD0-936]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5125`

## Notes

CPD-12575 + CPD0-936 -> PROTON + CPD0-937 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
