---
entity_id: "reaction.ecocyc.RXN-24977"
entity_type: "reaction"
name: "RXN-24977"
source_database: "EcoCyc"
source_id: "RXN-24977"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24977

`reaction.ecocyc.RXN-24977`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24977`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-11657 + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-11657 + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by excision nuclease UvrABC (complex.ecocyc.UVRABC-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), a (6-4) photoproduct (in DNA) (molecule.ecocyc.CPD-11657). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-11657 + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.UVRABC-CPLX|complex.ecocyc.UVRABC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-11657|molecule.ecocyc.CPD-11657]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24977`

## Notes

CPD-11657 + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
