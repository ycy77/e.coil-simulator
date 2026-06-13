---
entity_id: "reaction.ecocyc.RXN-22655"
entity_type: "reaction"
name: "RXN-22655"
source_database: "EcoCyc"
source_id: "RXN-22655"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22655

`reaction.ecocyc.RXN-22655`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22655`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HyCE-Ni-Fe-CO-CN2 + WATER -> OLIGOPEPTIDES + HycE-Ni-Fe-CO-CN2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HyCE-Ni-Fe-CO-CN2 + WATER -> OLIGOPEPTIDES + HycE-Ni-Fe-CO-CN2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hycI (protein.P0AEV9), hybD (protein.P37182). Substrates: H2O (molecule.C00001). Products: Oligopeptide (molecule.C00098).

## Enriched Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Annotation

HyCE-Ni-Fe-CO-CN2 + WATER -> OLIGOPEPTIDES + HycE-Ni-Fe-CO-CN2; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AEV9|protein.P0AEV9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37182|protein.P37182]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00098|molecule.C00098]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22655`

## Notes

HyCE-Ni-Fe-CO-CN2 + WATER -> OLIGOPEPTIDES + HycE-Ni-Fe-CO-CN2; direction=PHYSIOL-LEFT-TO-RIGHT
