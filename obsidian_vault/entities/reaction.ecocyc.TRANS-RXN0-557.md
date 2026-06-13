---
entity_id: "reaction.ecocyc.TRANS-RXN0-557"
entity_type: "reaction"
name: "TRANS-RXN0-557"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-557"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-557

`reaction.ecocyc.TRANS-RXN0-557`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-557`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ALLANTOIN + PROTON -> ALLANTOIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ALLANTOIN + PROTON -> ALLANTOIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), allantoin (molecule.ecocyc.ALLANTOIN). Products: H+ (molecule.C00080), allantoin (molecule.ecocyc.ALLANTOIN).

## Annotation

ALLANTOIN + PROTON -> ALLANTOIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ALLANTOIN|molecule.ecocyc.ALLANTOIN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ALLANTOIN|molecule.ecocyc.ALLANTOIN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-557`

## Notes

ALLANTOIN + PROTON -> ALLANTOIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
