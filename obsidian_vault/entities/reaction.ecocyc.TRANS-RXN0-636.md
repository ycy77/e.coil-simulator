---
entity_id: "reaction.ecocyc.TRANS-RXN0-636"
entity_type: "reaction"
name: "SecA-dependent protein translocation"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-636"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SecA-dependent protein translocation

`reaction.ecocyc.TRANS-RXN0-636`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-636`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

a-SecA-dependent-substrate-protein + ATP + WATER -> a-SecA-dependent-substrate-protein + ADP + Pi + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: a-SecA-dependent-substrate-protein + ATP + WATER -> a-SecA-dependent-substrate-protein + ADP + Pi + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by SecYEG-SecA complex (complex.ecocyc.CPLX0-12269). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

a-SecA-dependent-substrate-protein + ATP + WATER -> a-SecA-dependent-substrate-protein + ADP + Pi + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12269|complex.ecocyc.CPLX0-12269]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-636`

## Notes

a-SecA-dependent-substrate-protein + ATP + WATER -> a-SecA-dependent-substrate-protein + ADP + Pi + PROTON; direction=LEFT-TO-RIGHT
