---
entity_id: "reaction.ecocyc.RXN-14361"
entity_type: "reaction"
name: "RXN-14361"
source_database: "EcoCyc"
source_id: "RXN-14361"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14361

`reaction.ecocyc.RXN-14361`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14361`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-GLUCURONATE + CPD0-934 -> CPD-15237 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP-GLUCURONATE + CPD0-934 -> CPD-15237 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yibD (protein.P11290). Substrates: UDP-glucuronate (molecule.C00167), glucosyl-(heptosyl)3-Kdo2-lipid A-phosphate (E. coli) (molecule.ecocyc.CPD0-934). Products: UDP (molecule.C00015), H+ (molecule.C00080), glucosyl-(heptosyl)3-glucosyluronate-Kdo2-lipid A-phosphate (molecule.ecocyc.CPD-15237).

## Annotation

UDP-GLUCURONATE + CPD0-934 -> CPD-15237 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P11290|protein.P11290]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15237|molecule.ecocyc.CPD-15237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00167|molecule.C00167]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-934|molecule.ecocyc.CPD0-934]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14361`

## Notes

UDP-GLUCURONATE + CPD0-934 -> CPD-15237 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
