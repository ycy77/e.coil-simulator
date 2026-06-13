---
entity_id: "reaction.ecocyc.RXN-17944"
entity_type: "reaction"
name: "RXN-17944"
source_database: "EcoCyc"
source_id: "RXN-17944"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17944

`reaction.ecocyc.RXN-17944`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17944`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12797 + OXYGEN-MOLECULE -> CPD-19233 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12797 + OXYGEN-MOLECULE -> CPD-19233 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cueO (protein.P36649). Substrates: Oxygen (molecule.C00007), syringol (molecule.ecocyc.CPD-12797). Products: H2O (molecule.C00001), 3,3',5,5'-tetramethoxydiphenoquinone (molecule.ecocyc.CPD-19233).

## Annotation

CPD-12797 + OXYGEN-MOLECULE -> CPD-19233 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P36649|protein.P36649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19233|molecule.ecocyc.CPD-19233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12797|molecule.ecocyc.CPD-12797]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17944`

## Notes

CPD-12797 + OXYGEN-MOLECULE -> CPD-19233 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
