---
entity_id: "reaction.ecocyc.RXN0-5522"
entity_type: "reaction"
name: "RXN0-5522"
source_database: "EcoCyc"
source_id: "RXN0-5522"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5522

`reaction.ecocyc.RXN0-5522`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5522`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

EG11171-MONOMER -> CPD0-1719; direction=LEFT-TO-RIGHT EcoCyc reaction equation: EG11171-MONOMER -> CPD0-1719; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tsaB (protein.P76256). Products: TsaD degradation products (molecule.ecocyc.CPD0-1719).

## Annotation

EG11171-MONOMER -> CPD0-1719; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P76256|protein.P76256]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1719|molecule.ecocyc.CPD0-1719]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN0-5522`

## Notes

EG11171-MONOMER -> CPD0-1719; direction=LEFT-TO-RIGHT
