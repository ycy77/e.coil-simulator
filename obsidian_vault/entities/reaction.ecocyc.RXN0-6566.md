---
entity_id: "reaction.ecocyc.RXN0-6566"
entity_type: "reaction"
name: "RXN0-6566"
source_database: "EcoCyc"
source_id: "RXN0-6566"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6566

`reaction.ecocyc.RXN0-6566`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6566`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cyclic-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP + WATER -> RNA-Holder + GMP + PPI + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Cyclic-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP + WATER -> RNA-Holder + GMP + PPI + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rtcB (protein.P46850). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046), H+ (molecule.C00080), GMP (molecule.C00144).

## Annotation

Cyclic-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP + WATER -> RNA-Holder + GMP + PPI + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P46850|protein.P46850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6566`

## Notes

Cyclic-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP + WATER -> RNA-Holder + GMP + PPI + PROTON; direction=LEFT-TO-RIGHT
