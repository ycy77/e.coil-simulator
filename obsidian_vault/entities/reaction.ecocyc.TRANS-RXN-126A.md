---
entity_id: "reaction.ecocyc.TRANS-RXN-126A"
entity_type: "reaction"
name: "L-valine:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-126A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-valine:Na+ symport

`reaction.ecocyc.TRANS-RXN-126A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-126A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + VAL -> NA+ + VAL; direction=REVERSIBLE EcoCyc reaction equation: NA+ + VAL -> NA+ + VAL; direction=REVERSIBLE.

## Biological Role

Catalyzed by brnQ (protein.P0AD99). Substrates: L-Valine (molecule.C00183), Sodium cation (molecule.C01330). Products: L-Valine (molecule.C00183), Sodium cation (molecule.C01330).

## Annotation

NA+ + VAL -> NA+ + VAL; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AD99|protein.P0AD99]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-126A`

## Notes

NA+ + VAL -> NA+ + VAL; direction=REVERSIBLE
