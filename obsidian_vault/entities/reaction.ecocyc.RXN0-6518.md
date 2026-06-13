---
entity_id: "reaction.ecocyc.RXN0-6518"
entity_type: "reaction"
name: "RXN0-6518"
source_database: "EcoCyc"
source_id: "RXN0-6518"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6518

`reaction.ecocyc.RXN0-6518`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6518`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + TORS-CPLX -> ADP + CPLX0-8265; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + TORS-CPLX -> ADP + CPLX0-8265; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1506` TorTSR Signal Transduction System, TMAO dependent (EcoCyc)

## Annotation

ATP + TORS-CPLX -> ADP + CPLX0-8265; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1506` TorTSR Signal Transduction System, TMAO dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6518`

## Notes

ATP + TORS-CPLX -> ADP + CPLX0-8265; direction=LEFT-TO-RIGHT
