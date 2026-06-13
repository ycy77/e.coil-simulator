---
entity_id: "reaction.ecocyc.RXN-24978"
entity_type: "reaction"
name: "RXN-24978"
source_database: "EcoCyc"
source_id: "RXN-24978"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24978

`reaction.ecocyc.RXN-24978`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24978`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-With-Cyclobutane-Pyrimidine-Dimers + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-With-Cyclobutane-Pyrimidine-Dimers + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by excision nuclease UvrABC (complex.ecocyc.UVRABC-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Annotation

DNA-With-Cyclobutane-Pyrimidine-Dimers + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.UVRABC-CPLX|complex.ecocyc.UVRABC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24978`

## Notes

DNA-With-Cyclobutane-Pyrimidine-Dimers + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
