---
entity_id: "reaction.ecocyc.PYRAZIN-RXN"
entity_type: "reaction"
name: "PYRAZIN-RXN"
source_database: "EcoCyc"
source_id: "PYRAZIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRAZIN-RXN

`reaction.ecocyc.PYRAZIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRAZIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRAZINAMIDE + WATER -> AMMONIUM + PYRAZINOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PYRAZINAMIDE + WATER -> AMMONIUM + PYRAZINOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pncA (protein.P21369). Substrates: H2O (molecule.C00001), pyrazinamide (molecule.ecocyc.PYRAZINAMIDE). Products: ammonium (molecule.ecocyc.AMMONIUM), pyrazine-2-carboxylate (molecule.ecocyc.PYRAZINOIC-ACID).

## Annotation

PYRAZINAMIDE + WATER -> AMMONIUM + PYRAZINOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21369|protein.P21369]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PYRAZINOIC-ACID|molecule.ecocyc.PYRAZINOIC-ACID]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PYRAZINAMIDE|molecule.ecocyc.PYRAZINAMIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYRAZIN-RXN`

## Notes

PYRAZINAMIDE + WATER -> AMMONIUM + PYRAZINOIC-ACID; direction=PHYSIOL-LEFT-TO-RIGHT
