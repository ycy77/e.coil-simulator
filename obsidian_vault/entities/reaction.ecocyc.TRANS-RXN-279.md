---
entity_id: "reaction.ecocyc.TRANS-RXN-279"
entity_type: "reaction"
name: "zinc hydrogenphosphate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-279"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# zinc hydrogenphosphate:proton symport

`reaction.ecocyc.TRANS-RXN-279`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-279`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-18501 + PROTON -> CPD-18501 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-18501 + PROTON -> CPD-18501 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by pitA (protein.P0AFJ7). Substrates: H+ (molecule.C00080), zinc hydrogenphosphate (molecule.ecocyc.CPD-18501). Products: H+ (molecule.C00080), zinc hydrogenphosphate (molecule.ecocyc.CPD-18501).

## Annotation

CPD-18501 + PROTON -> CPD-18501 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AFJ7|protein.P0AFJ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18501|molecule.ecocyc.CPD-18501]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18501|molecule.ecocyc.CPD-18501]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-279`

## Notes

CPD-18501 + PROTON -> CPD-18501 + PROTON; direction=REVERSIBLE
