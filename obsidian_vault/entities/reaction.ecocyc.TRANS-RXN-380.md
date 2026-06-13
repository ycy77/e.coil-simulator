---
entity_id: "reaction.ecocyc.TRANS-RXN-380"
entity_type: "reaction"
name: "TRANS-RXN-380"
source_database: "EcoCyc"
source_id: "TRANS-RXN-380"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-380

`reaction.ecocyc.TRANS-RXN-380`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-380`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Beta-Lactams -> Beta-Lactams; direction=REVERSIBLE EcoCyc reaction equation: Beta-Lactams -> Beta-Lactams; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: a β-lactam (molecule.ecocyc.Beta-Lactams). Products: a β-lactam (molecule.ecocyc.Beta-Lactams).

## Annotation

Beta-Lactams -> Beta-Lactams; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Beta-Lactams|molecule.ecocyc.Beta-Lactams]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Beta-Lactams|molecule.ecocyc.Beta-Lactams]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-380`

## Notes

Beta-Lactams -> Beta-Lactams; direction=REVERSIBLE
