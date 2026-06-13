---
entity_id: "reaction.ecocyc.TRANS-RXN-368"
entity_type: "reaction"
name: "cetylpyridinium:H+ antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-368"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# cetylpyridinium:H+ antiport

`reaction.ecocyc.TRANS-RXN-368`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-368`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-20888 + PROTON -> CPD-20888 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-20888 + PROTON -> CPD-20888 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by guanidinium exporter (complex.ecocyc.CPLX0-8263). Substrates: H+ (molecule.C00080), cetylpyridinium (molecule.ecocyc.CPD-20888). Products: H+ (molecule.C00080), cetylpyridinium (molecule.ecocyc.CPD-20888).

## Annotation

CPD-20888 + PROTON -> CPD-20888 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8263|complex.ecocyc.CPLX0-8263]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20888|molecule.ecocyc.CPD-20888]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20888|molecule.ecocyc.CPD-20888]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-368`

## Notes

CPD-20888 + PROTON -> CPD-20888 + PROTON; direction=REVERSIBLE
