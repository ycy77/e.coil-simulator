---
entity_id: "reaction.ecocyc.TRANS-RXN0-600"
entity_type: "reaction"
name: "diffusion of an inorganic compound"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-600"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# diffusion of an inorganic compound

`reaction.ecocyc.TRANS-RXN0-600`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-600`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Inorganic-Compounds -> Inorganic-Compounds; direction=REVERSIBLE EcoCyc reaction equation: Inorganic-Compounds -> Inorganic-Compounds; direction=REVERSIBLE.

## Biological Role

Substrates: an inorganic compound (molecule.ecocyc.Inorganic-Compounds). Products: an inorganic compound (molecule.ecocyc.Inorganic-Compounds).

## Annotation

Inorganic-Compounds -> Inorganic-Compounds; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.Inorganic-Compounds|molecule.ecocyc.Inorganic-Compounds]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Inorganic-Compounds|molecule.ecocyc.Inorganic-Compounds]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-600`

## Notes

Inorganic-Compounds -> Inorganic-Compounds; direction=REVERSIBLE
