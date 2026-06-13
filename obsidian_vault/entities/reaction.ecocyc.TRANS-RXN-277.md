---
entity_id: "reaction.ecocyc.TRANS-RXN-277"
entity_type: "reaction"
name: "magnesium hydrogenphosphate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-277"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# magnesium hydrogenphosphate:proton symport

`reaction.ecocyc.TRANS-RXN-277`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-277`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-18499 + PROTON -> CPD-18499 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-18499 + PROTON -> CPD-18499 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by pitA (protein.P0AFJ7), pitB (protein.P43676). Substrates: H+ (molecule.C00080), magnesium hydrogenphosphate (molecule.ecocyc.CPD-18499). Products: H+ (molecule.C00080), magnesium hydrogenphosphate (molecule.ecocyc.CPD-18499).

## Annotation

CPD-18499 + PROTON -> CPD-18499 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFJ7|protein.P0AFJ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P43676|protein.P43676]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18499|molecule.ecocyc.CPD-18499]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18499|molecule.ecocyc.CPD-18499]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-277`

## Notes

CPD-18499 + PROTON -> CPD-18499 + PROTON; direction=REVERSIBLE
