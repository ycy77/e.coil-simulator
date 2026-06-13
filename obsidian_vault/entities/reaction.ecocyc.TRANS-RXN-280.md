---
entity_id: "reaction.ecocyc.TRANS-RXN-280"
entity_type: "reaction"
name: "tellurite:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-280"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# tellurite:proton symport

`reaction.ecocyc.TRANS-RXN-280`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-280`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-4544 + PROTON -> CPD-4544 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-4544 + PROTON -> CPD-4544 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by pitA (protein.P0AFJ7). Substrates: H+ (molecule.C00080), tellurite (molecule.ecocyc.CPD-4544). Products: H+ (molecule.C00080), tellurite (molecule.ecocyc.CPD-4544).

## Annotation

CPD-4544 + PROTON -> CPD-4544 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AFJ7|protein.P0AFJ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-280`

## Notes

CPD-4544 + PROTON -> CPD-4544 + PROTON; direction=REVERSIBLE
