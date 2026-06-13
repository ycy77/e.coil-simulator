---
entity_id: "reaction.ecocyc.PSEUDOURIDINE-KINASE-RXN"
entity_type: "reaction"
name: "PSEUDOURIDINE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "PSEUDOURIDINE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PSEUDOURIDINE-KINASE-RXN

`reaction.ecocyc.PSEUDOURIDINE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PSEUDOURIDINE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-497 + ATP -> PROTON + PSEUDOURIDINE-5-P + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-497 + ATP -> PROTON + PSEUDOURIDINE-5-P + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by psuK (protein.P30235). Substrates: ATP (molecule.C00002), Pseudouridine (molecule.C02067). Products: ADP (molecule.C00008), H+ (molecule.C00080), Pseudouridine 5'-phosphate (molecule.C01168).

## Enriched Pathways

- `ecocyc.PWY-6019` pseudouridine degradation (EcoCyc)

## Annotation

CPD-497 + ATP -> PROTON + PSEUDOURIDINE-5-P + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6019` pseudouridine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P30235|protein.P30235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01168|molecule.C01168]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02067|molecule.C02067]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PSEUDOURIDINE-KINASE-RXN`

## Notes

CPD-497 + ATP -> PROTON + PSEUDOURIDINE-5-P + ADP; direction=LEFT-TO-RIGHT
