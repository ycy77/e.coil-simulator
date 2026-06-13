---
entity_id: "reaction.ecocyc.RXN-17905"
entity_type: "reaction"
name: "RXN-17905"
source_database: "EcoCyc"
source_id: "RXN-17905"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17905

`reaction.ecocyc.RXN-17905`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17905`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP -> RNA-Holder + GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP -> RNA-Holder + GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rtcB (protein.P46850). Substrates: GTP (molecule.C00044). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046), GMP (molecule.C00144).

## Annotation

3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP -> RNA-Holder + GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P46850|protein.P46850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17905`

## Notes

3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + GTP -> RNA-Holder + GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
