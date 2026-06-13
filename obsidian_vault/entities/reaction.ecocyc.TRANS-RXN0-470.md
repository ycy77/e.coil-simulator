---
entity_id: "reaction.ecocyc.TRANS-RXN0-470"
entity_type: "reaction"
name: "TRANS-RXN0-470"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-470"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-470

`reaction.ecocyc.TRANS-RXN0-470`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-470`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Pi -> Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Pi -> Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yjbB (protein.P0AF43). Substrates: phosphate (molecule.ecocyc.Pi). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

Pi -> Pi; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AF43|protein.P0AF43]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-470`

## Notes

Pi -> Pi; direction=LEFT-TO-RIGHT
