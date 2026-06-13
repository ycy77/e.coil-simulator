---
entity_id: "reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "MANNITOL-1-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "MANNITOL-1-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MANNITOL-1-PHOSPHATASE-RXN

`reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MANNITOL-1-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + MANNITOL-1P -> Pi + MANNITOL; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + MANNITOL-1P -> Pi + MANNITOL; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hxpB (protein.P77247), hxpA (protein.P77625). Substrates: H2O (molecule.C00001), D-Mannitol 1-phosphate (molecule.C00644). Products: Mannitol (molecule.C00392), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + MANNITOL-1P -> Pi + MANNITOL; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77247|protein.P77247]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77625|protein.P77625]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00392|molecule.C00392]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00644|molecule.C00644]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MANNITOL-1-PHOSPHATASE-RXN`

## Notes

WATER + MANNITOL-1P -> Pi + MANNITOL; direction=PHYSIOL-LEFT-TO-RIGHT
