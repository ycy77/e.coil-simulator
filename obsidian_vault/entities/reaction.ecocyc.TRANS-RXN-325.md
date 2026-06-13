---
entity_id: "reaction.ecocyc.TRANS-RXN-325"
entity_type: "reaction"
name: "TRANS-RXN-325"
source_database: "EcoCyc"
source_id: "TRANS-RXN-325"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-325

`reaction.ecocyc.TRANS-RXN-325`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-325`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CANAVANINE -> CANAVANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CANAVANINE -> CANAVANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by argO (protein.P11667). Substrates: L-canavanine (molecule.ecocyc.CANAVANINE). Products: L-canavanine (molecule.ecocyc.CANAVANINE).

## Annotation

CANAVANINE -> CANAVANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P11667|protein.P11667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CANAVANINE|molecule.ecocyc.CANAVANINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CANAVANINE|molecule.ecocyc.CANAVANINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-325`

## Notes

CANAVANINE -> CANAVANINE; direction=PHYSIOL-LEFT-TO-RIGHT
