---
entity_id: "reaction.ecocyc.TRANS-RXN-131"
entity_type: "reaction"
name: "TRANS-RXN-131"
source_database: "EcoCyc"
source_id: "TRANS-RXN-131"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-131

`reaction.ecocyc.TRANS-RXN-131`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-131`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GLYCEROL -> GLYCEROL; direction=REVERSIBLE EcoCyc reaction equation: GLYCEROL -> GLYCEROL; direction=REVERSIBLE.

## Biological Role

Catalyzed by glycerol facilitator (complex.ecocyc.CPLX0-7654). Substrates: Glycerol (molecule.C00116). Products: Glycerol (molecule.C00116).

## Annotation

GLYCEROL -> GLYCEROL; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-131`

## Notes

GLYCEROL -> GLYCEROL; direction=REVERSIBLE
