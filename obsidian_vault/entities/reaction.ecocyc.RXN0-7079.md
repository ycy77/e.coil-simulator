---
entity_id: "reaction.ecocyc.RXN0-7079"
entity_type: "reaction"
name: "RXN0-7079"
source_database: "EcoCyc"
source_id: "RXN0-7079"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7079

`reaction.ecocyc.RXN0-7079`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7079`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2552 + WATER -> 7-METHYLGUANOSINE-5-PHOSPHATE + PPI + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2552 + WATER -> 7-METHYLGUANOSINE-5-PHOSPHATE + PPI + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yceF (protein.P0A729). Substrates: H2O (molecule.C00001), m7GTP (molecule.ecocyc.CPD0-2552). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), N7-methylguanosine 5'-phosphate (molecule.ecocyc.7-METHYLGUANOSINE-5-PHOSPHATE).

## Annotation

CPD0-2552 + WATER -> 7-METHYLGUANOSINE-5-PHOSPHATE + PPI + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A729|protein.P0A729]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.7-METHYLGUANOSINE-5-PHOSPHATE|molecule.ecocyc.7-METHYLGUANOSINE-5-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2552|molecule.ecocyc.CPD0-2552]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7079`

## Notes

CPD0-2552 + WATER -> 7-METHYLGUANOSINE-5-PHOSPHATE + PPI + PROTON; direction=LEFT-TO-RIGHT
