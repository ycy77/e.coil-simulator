---
entity_id: "reaction.ecocyc.MALTODEXGLUCOSID-RXN"
entity_type: "reaction"
name: "MALTODEXGLUCOSID-RXN"
source_database: "EcoCyc"
source_id: "MALTODEXGLUCOSID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALTODEXGLUCOSID-RXN

`reaction.ecocyc.MALTODEXGLUCOSID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALTODEXGLUCOSID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the catabolic pathway for maltodextrins. EcoCyc reaction equation: 1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT. Part of the catabolic pathway for maltodextrins.

## Biological Role

Catalyzed by maltodextrin glucosidase (complex.ecocyc.CPLX0-8615). Substrates: H2O (molecule.C00001), Amylose (molecule.C00718). Products: alpha-D-Glucose (molecule.C00267), Amylose (molecule.C00718).

## Annotation

Part of the catabolic pathway for maltodextrins.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8615|complex.ecocyc.CPLX0-8615]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00267|molecule.C00267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MALTODEXGLUCOSID-RXN`

## Notes

1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT
