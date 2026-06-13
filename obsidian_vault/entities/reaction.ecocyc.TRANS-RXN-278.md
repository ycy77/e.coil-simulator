---
entity_id: "reaction.ecocyc.TRANS-RXN-278"
entity_type: "reaction"
name: "calcium hydrogenphosphate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-278"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# calcium hydrogenphosphate:proton symport

`reaction.ecocyc.TRANS-RXN-278`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-278`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-18500 + PROTON -> CPD-18500 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-18500 + PROTON -> CPD-18500 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by pitA (protein.P0AFJ7), pitB (protein.P43676). Substrates: H+ (molecule.C00080), calcium hydrogenphosphate (molecule.ecocyc.CPD-18500). Products: H+ (molecule.C00080), calcium hydrogenphosphate (molecule.ecocyc.CPD-18500).

## Annotation

CPD-18500 + PROTON -> CPD-18500 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFJ7|protein.P0AFJ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P43676|protein.P43676]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18500|molecule.ecocyc.CPD-18500]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18500|molecule.ecocyc.CPD-18500]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-278`

## Notes

CPD-18500 + PROTON -> CPD-18500 + PROTON; direction=REVERSIBLE
