---
entity_id: "reaction.ecocyc.ALTRODEHYDRAT-RXN"
entity_type: "reaction"
name: "ALTRODEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "ALTRODEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALTRODEHYDRAT-RXN

`reaction.ecocyc.ALTRODEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALTRODEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the galacturonate pathway. EcoCyc reaction equation: D-ALTRONATE -> WATER + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=LEFT-TO-RIGHT. Part of the galacturonate pathway.

## Biological Role

Catalyzed by uxaA (protein.P42604). Substrates: D-Altronate (molecule.C00817). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204).

## Enriched Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)

## Annotation

Part of the galacturonate pathway.

## Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P42604|protein.P42604]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00817|molecule.C00817]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00878|molecule.C00878]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALTRODEHYDRAT-RXN`

## Notes

D-ALTRONATE -> WATER + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=LEFT-TO-RIGHT
