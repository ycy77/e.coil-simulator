---
entity_id: "reaction.ecocyc.RXN-25213"
entity_type: "reaction"
name: "RXN-25213"
source_database: "EcoCyc"
source_id: "RXN-25213"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25213

`reaction.ecocyc.RXN-25213`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25213`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-27798 + NAD -> CPD0-1327 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-27798 + NAD -> CPD0-1327 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by dihydropyrimidine dehydrogenase (NAD+) (complex.ecocyc.CPLX0-7788). Substrates: NAD+ (molecule.C00003), 5-fluorodihydrouracil (molecule.ecocyc.CPD-27798). Products: NADH (molecule.C00004), H+ (molecule.C00080), 5-fluorouracil (molecule.ecocyc.CPD0-1327).

## Annotation

CPD-27798 + NAD -> CPD0-1327 + NADH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7788|complex.ecocyc.CPLX0-7788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1327|molecule.ecocyc.CPD0-1327]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-27798|molecule.ecocyc.CPD-27798]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25213`

## Notes

CPD-27798 + NAD -> CPD0-1327 + NADH + PROTON; direction=REVERSIBLE
