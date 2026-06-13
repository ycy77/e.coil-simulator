---
entity_id: "reaction.ecocyc.TRANS-RXN-71"
entity_type: "reaction"
name: "L-serine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-71"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-serine:proton symport

`reaction.ecocyc.TRANS-RXN-71`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-71`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + SER -> PROTON + SER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + SER -> PROTON + SER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sdaC (protein.P0AAD6), tdcC (protein.P0AAD8), thrP (protein.P27837). Substrates: L-Serine (molecule.C00065), H+ (molecule.C00080). Products: L-Serine (molecule.C00065), H+ (molecule.C00080).

## Annotation

PROTON + SER -> PROTON + SER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AAD6|protein.P0AAD6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AAD8|protein.P0AAD8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27837|protein.P27837]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-71`

## Notes

PROTON + SER -> PROTON + SER; direction=LEFT-TO-RIGHT
