---
entity_id: "reaction.ecocyc.TRANS-RXN-350"
entity_type: "reaction"
name: "nalidixate:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-350"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# nalidixate:proton antiport

`reaction.ecocyc.TRANS-RXN-350`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-350`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by multidrug/spermidine efflux pump (complex.ecocyc.YDGEF-CPLX). Substrates: H+ (molecule.C00080), nalidixic acid (molecule.ecocyc.CPD-21025). Products: H+ (molecule.C00080), nalidixic acid (molecule.ecocyc.CPD-21025).

## Annotation

CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.YDGEF-CPLX|complex.ecocyc.YDGEF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21025|molecule.ecocyc.CPD-21025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21025|molecule.ecocyc.CPD-21025]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-350`

## Notes

CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=REVERSIBLE
