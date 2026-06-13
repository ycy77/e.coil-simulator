---
entity_id: "reaction.ecocyc.RXN0-5123"
entity_type: "reaction"
name: "RXN0-5123"
source_database: "EcoCyc"
source_id: "RXN0-5123"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5123

`reaction.ecocyc.RXN0-5123`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5123`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-934 + ATP -> PROTON + CPD0-935 + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-934 + ATP -> PROTON + CPD0-935 + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaY (protein.P27240). Substrates: ATP (molecule.C00002), glucosyl-(heptosyl)3-Kdo2-lipid A-phosphate (E. coli) (molecule.ecocyc.CPD0-934). Products: ADP (molecule.C00008), H+ (molecule.C00080), glucosyl-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-935).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

CPD0-934 + ATP -> PROTON + CPD0-935 + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27240|protein.P27240]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-935|molecule.ecocyc.CPD0-935]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-934|molecule.ecocyc.CPD0-934]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5123`

## Notes

CPD0-934 + ATP -> PROTON + CPD0-935 + ADP; direction=LEFT-TO-RIGHT
