---
entity_id: "reaction.ecocyc.TRANS-RXN0-203"
entity_type: "reaction"
name: "galactarate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-203"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# galactarate:proton symport

`reaction.ecocyc.TRANS-RXN0-203`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-203`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

D-GALACTARATE + PROTON -> D-GALACTARATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: D-GALACTARATE + PROTON -> D-GALACTARATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by garP (protein.P0AA80), gudP (protein.Q46916). Substrates: H+ (molecule.C00080), D-Galactarate (molecule.C00879). Products: H+ (molecule.C00080), D-Galactarate (molecule.C00879).

## Annotation

D-GALACTARATE + PROTON -> D-GALACTARATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AA80|protein.P0AA80]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46916|protein.Q46916]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00879|molecule.C00879]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00879|molecule.C00879]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-203`

## Notes

D-GALACTARATE + PROTON -> D-GALACTARATE + PROTON; direction=REVERSIBLE
