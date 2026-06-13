---
entity_id: "reaction.ecocyc.TRANS-RXN0-551"
entity_type: "reaction"
name: "TRANS-RXN0-551"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-551"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-551

`reaction.ecocyc.TRANS-RXN0-551`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-551`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-2040 -> CPD0-2040; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2040 -> CPD0-2040; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glycerol facilitator (complex.ecocyc.CPLX0-7654). Substrates: arsenous acid (molecule.ecocyc.CPD0-2040). Products: arsenous acid (molecule.ecocyc.CPD0-2040).

## Annotation

CPD0-2040 -> CPD0-2040; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-551`

## Notes

CPD0-2040 -> CPD0-2040; direction=LEFT-TO-RIGHT
