---
entity_id: "reaction.ecocyc.MANNONDEHYDRAT-RXN"
entity_type: "reaction"
name: "MANNONDEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "MANNONDEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MANNONDEHYDRAT-RXN

`reaction.ecocyc.MANNONDEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MANNONDEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the glucuronate pathway. EcoCyc reaction equation: D-MANNONATE -> WATER + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=LEFT-TO-RIGHT. Part of the glucuronate pathway.

## Biological Role

Catalyzed by uxuA (protein.P24215). Substrates: D-Mannonate (molecule.C00514). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204).

## Enriched Pathways

- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)

## Annotation

Part of the glucuronate pathway.

## Pathways

- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `activates` <-- [[molecule.C00191|molecule.C00191]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00333|molecule.C00333]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00558|molecule.C00558]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00817|molecule.C00817]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P24215|protein.P24215]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00514|molecule.C00514]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00392|molecule.C00392]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00794|molecule.C00794]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1655|molecule.ecocyc.CPD0-1655]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1656|molecule.ecocyc.CPD0-1656]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MANNONDEHYDRAT-RXN`

## Notes

D-MANNONATE -> WATER + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=LEFT-TO-RIGHT
