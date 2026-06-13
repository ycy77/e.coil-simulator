---
entity_id: "reaction.ecocyc.TRANS-RXN0-595"
entity_type: "reaction"
name: "TRANS-RXN0-595"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-595"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-595

`reaction.ecocyc.TRANS-RXN0-595`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-595`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FMN -> FMN; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FMN -> FMN; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yeeO (protein.P76352). Substrates: FMN (molecule.C00061). Products: FMN (molecule.C00061).

## Annotation

FMN -> FMN; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76352|protein.P76352]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-595`

## Notes

FMN -> FMN; direction=LEFT-TO-RIGHT
