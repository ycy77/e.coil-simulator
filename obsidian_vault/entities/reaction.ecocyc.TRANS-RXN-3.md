---
entity_id: "reaction.ecocyc.TRANS-RXN-3"
entity_type: "reaction"
name: "K+:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-3"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# K+:proton symport

`reaction.ecocyc.TRANS-RXN-3`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-3`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + K+ -> PROTON + K+; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + K+ -> PROTON + K+; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by trkH (protein.P0AFZ7), kup (protein.P63183). Substrates: H+ (molecule.C00080), Potassium cation (molecule.C00238). Products: H+ (molecule.C00080), Potassium cation (molecule.C00238).

## Annotation

PROTON + K+ -> PROTON + K+; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFZ7|protein.P0AFZ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P63183|protein.P63183]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-3`

## Notes

PROTON + K+ -> PROTON + K+; direction=LEFT-TO-RIGHT
