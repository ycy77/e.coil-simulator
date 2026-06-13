---
entity_id: "reaction.ecocyc.TRANS-RXN0-587"
entity_type: "reaction"
name: "TRANS-RXN0-587"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-587"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-587

`reaction.ecocyc.TRANS-RXN0-587`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-587`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-882 -> CPD0-882; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-882 -> CPD0-882; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by murP (protein.P77272). Substrates: 1,6-Anhydro-N-acetyl-beta-muramate (molecule.C19769). Products: 1,6-Anhydro-N-acetyl-beta-muramate (molecule.C19769).

## Annotation

CPD0-882 -> CPD0-882; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P77272|protein.P77272]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C19769|molecule.C19769]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C19769|molecule.C19769]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-587`

## Notes

CPD0-882 -> CPD0-882; direction=LEFT-TO-RIGHT
