---
entity_id: "reaction.ecocyc.RXN0-6418"
entity_type: "reaction"
name: "RXN0-6418"
source_database: "EcoCyc"
source_id: "RXN0-6418"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6418

`reaction.ecocyc.RXN0-6418`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6418`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This glue reaction connects the class with an instance, due to spontaneous equilibration. EcoCyc reaction equation: GLC -> D-Glucose; direction=REVERSIBLE. This glue reaction connects the class with an instance, due to spontaneous equilibration.

## Biological Role

Substrates: beta-D-Glucose (molecule.C00221). Products: D-Glucose (molecule.C00031).

## Annotation

This glue reaction connects the class with an instance, due to spontaneous equilibration.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00221|molecule.C00221]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6418`

## Notes

GLC -> D-Glucose; direction=REVERSIBLE
