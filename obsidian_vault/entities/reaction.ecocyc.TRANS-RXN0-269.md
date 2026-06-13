---
entity_id: "reaction.ecocyc.TRANS-RXN0-269"
entity_type: "reaction"
name: "TRANS-RXN0-269"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-269"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-269

`reaction.ecocyc.TRANS-RXN0-269`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-269`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

VAL -> VAL; direction=LEFT-TO-RIGHT EcoCyc reaction equation: VAL -> VAL; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-valine exporter (complex.ecocyc.CPLX0-7684). Substrates: L-Valine (molecule.C00183). Products: L-Valine (molecule.C00183).

## Annotation

VAL -> VAL; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7684|complex.ecocyc.CPLX0-7684]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-269`

## Notes

VAL -> VAL; direction=LEFT-TO-RIGHT
