---
entity_id: "reaction.ecocyc.MALTODEG-RXN"
entity_type: "reaction"
name: "MALTODEG-RXN"
source_database: "EcoCyc"
source_id: "MALTODEG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALTODEG-RXN

`reaction.ecocyc.MALTODEG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALTODEG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This represents a specific instance of the type of reaction that can be catalyzed by amylomaltase. A more generic reaction can be expressed as: maltodextrin(n) + maltodextrin(m) = maltodextrin(m+n-1) + β-D-glucose where m and n represent the number of glycosyl units within the maltodextrin polymer. EcoCyc reaction equation: MALTOSE + MALTOHEXAOSE -> CPD0-1133 + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT. This represents a specific instance of the type of reaction that can be catalyzed by amylomaltase. A more generic reaction can be expressed as: maltodextrin(n) + maltodextrin(m) = maltodextrin(m+n-1) + β-D-glucose where m and n represent the number of glycosyl units within the maltodextrin polymer.

## Biological Role

Catalyzed by malQ (protein.P15977). Substrates: Maltose (molecule.C00208), maltohexaose (molecule.ecocyc.MALTOHEXAOSE). Products: D-Glucose (molecule.C00031), maltoheptaose (molecule.ecocyc.CPD0-1133).

## Annotation

This represents a specific instance of the type of reaction that can be catalyzed by amylomaltase. A more generic reaction can be expressed as: maltodextrin(n) + maltodextrin(m) = maltodextrin(m+n-1) + β-D-glucose where m and n represent the number of glycosyl units within the maltodextrin polymer.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P15977|protein.P15977]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1133|molecule.ecocyc.CPD0-1133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MALTODEG-RXN`

## Notes

MALTOSE + MALTOHEXAOSE -> CPD0-1133 + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
