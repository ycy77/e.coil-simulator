---
entity_id: "reaction.ecocyc.TRANS-RXN0-162"
entity_type: "reaction"
name: "TRANS-RXN0-162"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-162"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-162

`reaction.ecocyc.TRANS-RXN0-162`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-162`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTOHEME + ATP + WATER -> PROTOHEME + Pi + ADP + PROTON; direction= EcoCyc reaction equation: PROTOHEME + ATP + WATER -> PROTOHEME + Pi + ADP + PROTON; direction=.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), protoheme (molecule.ecocyc.PROTOHEME). Products: ADP (molecule.C00008), H+ (molecule.C00080), protoheme (molecule.ecocyc.PROTOHEME), phosphate (molecule.ecocyc.Pi).

## Annotation

PROTOHEME + ATP + WATER -> PROTOHEME + Pi + ADP + PROTON; direction=

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-162`

## Notes

PROTOHEME + ATP + WATER -> PROTOHEME + Pi + ADP + PROTON; direction=
