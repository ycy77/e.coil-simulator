---
entity_id: "reaction.ecocyc.TRANS-RXN-481"
entity_type: "reaction"
name: "TRANS-RXN-481"
source_database: "EcoCyc"
source_id: "TRANS-RXN-481"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-481

`reaction.ecocyc.TRANS-RXN-481`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-481`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

CPD-13227 -> CPD-13227; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13227 -> CPD-13227; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by chiP (protein.P75733). Substrates: N,N',N''-triacetylchitotriose (molecule.ecocyc.CPD-13227). Products: N,N',N''-triacetylchitotriose (molecule.ecocyc.CPD-13227).

## Annotation

CPD-13227 -> CPD-13227; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P75733|protein.P75733]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-13227|molecule.ecocyc.CPD-13227]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13227|molecule.ecocyc.CPD-13227]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-481`

## Notes

CPD-13227 -> CPD-13227; direction=PHYSIOL-LEFT-TO-RIGHT
