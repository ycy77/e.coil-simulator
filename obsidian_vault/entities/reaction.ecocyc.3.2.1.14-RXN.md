---
entity_id: "reaction.ecocyc.3.2.1.14-RXN"
entity_type: "reaction"
name: "3.2.1.14-RXN"
source_database: "EcoCyc"
source_id: "3.2.1.14-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.2.1.14-RXN

`reaction.ecocyc.3.2.1.14-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.2.1.14-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CHITIN + WATER -> Chitodextrins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CHITIN + WATER -> Chitodextrins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by chiA (protein.P13656). Substrates: H2O (molecule.C00001), Chitin (molecule.C00461). Products: a chitodextrin (molecule.ecocyc.Chitodextrins).

## Annotation

CHITIN + WATER -> Chitodextrins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P13656|protein.P13656]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Chitodextrins|molecule.ecocyc.Chitodextrins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00461|molecule.C00461]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.2.1.14-RXN`

## Notes

CHITIN + WATER -> Chitodextrins; direction=PHYSIOL-LEFT-TO-RIGHT
