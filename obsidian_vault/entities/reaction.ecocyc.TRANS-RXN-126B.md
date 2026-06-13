---
entity_id: "reaction.ecocyc.TRANS-RXN-126B"
entity_type: "reaction"
name: "L-leucine:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-126B"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-leucine:Na+ symport

`reaction.ecocyc.TRANS-RXN-126B`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-126B`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + LEU -> NA+ + LEU; direction=REVERSIBLE EcoCyc reaction equation: NA+ + LEU -> NA+ + LEU; direction=REVERSIBLE.

## Biological Role

Catalyzed by brnQ (protein.P0AD99). Substrates: L-Leucine (molecule.C00123), Sodium cation (molecule.C01330). Products: L-Leucine (molecule.C00123), Sodium cation (molecule.C01330).

## Annotation

NA+ + LEU -> NA+ + LEU; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AD99|protein.P0AD99]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-126B`

## Notes

NA+ + LEU -> NA+ + LEU; direction=REVERSIBLE
