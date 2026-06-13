---
entity_id: "reaction.ecocyc.RXN0-6542"
entity_type: "reaction"
name: "RXN0-6542"
source_database: "EcoCyc"
source_id: "RXN0-6542"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6542

`reaction.ecocyc.RXN0-6542`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6542`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL

## Enriched Summary

ATP + CHEA-CPLX -> ADP + CPLX0-8274; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CHEA-CPLX -> ADP + CPLX0-8274; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1518` chemotaxis signal transduction (EcoCyc)
- `ecocyc.PWY0-1519` aerotaxis signal transduction (EcoCyc)

## Annotation

ATP + CHEA-CPLX -> ADP + CPLX0-8274; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1518` chemotaxis signal transduction (EcoCyc)
- `ecocyc.PWY0-1519` aerotaxis signal transduction (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6542`

## Notes

ATP + CHEA-CPLX -> ADP + CPLX0-8274; direction=LEFT-TO-RIGHT
