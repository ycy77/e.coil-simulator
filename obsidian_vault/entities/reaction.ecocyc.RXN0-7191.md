---
entity_id: "reaction.ecocyc.RXN0-7191"
entity_type: "reaction"
name: "RXN0-7191"
source_database: "EcoCyc"
source_id: "RXN0-7191"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7191

`reaction.ecocyc.RXN0-7191`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7191`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-2039 -> CPD0-2039; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2039 -> CPD0-2039; direction=REVERSIBLE.

## Biological Role

Catalyzed by glycerol facilitator (complex.ecocyc.CPLX0-7654). Substrates: antimonous acid (molecule.ecocyc.CPD0-2039). Products: antimonous acid (molecule.ecocyc.CPD0-2039).

## Annotation

CPD0-2039 -> CPD0-2039; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2039|molecule.ecocyc.CPD0-2039]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2039|molecule.ecocyc.CPD0-2039]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7191`

## Notes

CPD0-2039 -> CPD0-2039; direction=REVERSIBLE
