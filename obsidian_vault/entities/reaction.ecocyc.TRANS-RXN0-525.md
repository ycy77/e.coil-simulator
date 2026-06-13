---
entity_id: "reaction.ecocyc.TRANS-RXN0-525"
entity_type: "reaction"
name: "TRANS-RXN0-525"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-525"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-525

`reaction.ecocyc.TRANS-RXN0-525`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-525`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hydrolysis of 3,5-tetradecadienoyl-CoA, a minor side product of PWY0-1337 produces 3,5-tetradecadienoate that is released into the growth medium . EcoCyc reaction equation: CPD0-1159 -> CPD0-1159; direction=LEFT-TO-RIGHT. Hydrolysis of 3,5-tetradecadienoyl-CoA, a minor side product of PWY0-1337 produces 3,5-tetradecadienoate that is released into the growth medium .

## Biological Role

Substrates: (3E,5Z)-tetradeca-3,5-dienoate (molecule.ecocyc.CPD0-1159). Products: (3E,5Z)-tetradeca-3,5-dienoate (molecule.ecocyc.CPD0-1159).

## Annotation

Hydrolysis of 3,5-tetradecadienoyl-CoA, a minor side product of PWY0-1337 produces 3,5-tetradecadienoate that is released into the growth medium .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD0-1159|molecule.ecocyc.CPD0-1159]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1159|molecule.ecocyc.CPD0-1159]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-525`

## Notes

CPD0-1159 -> CPD0-1159; direction=LEFT-TO-RIGHT
