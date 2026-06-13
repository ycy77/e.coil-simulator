---
entity_id: "reaction.ecocyc.RXN0-1401"
entity_type: "reaction"
name: "RXN0-1401"
source_database: "EcoCyc"
source_id: "RXN0-1401"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1401

`reaction.ecocyc.RXN0-1401`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1401`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RIBOSE-15-BISPHOSPHATE + ATP -> PRPP + ADP; direction=REVERSIBLE EcoCyc reaction equation: RIBOSE-15-BISPHOSPHATE + ATP -> PRPP + ADP; direction=REVERSIBLE.

## Biological Role

Catalyzed by phnN (protein.P16690). Substrates: ATP (molecule.C00002), D-Ribose 1,5-bisphosphate (molecule.C01151). Products: ADP (molecule.C00008), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119).

## Enriched Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)
- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Annotation

RIBOSE-15-BISPHOSPHATE + ATP -> PRPP + ADP; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)
- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P16690|protein.P16690]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01151|molecule.C01151]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1401`

## Notes

RIBOSE-15-BISPHOSPHATE + ATP -> PRPP + ADP; direction=REVERSIBLE
