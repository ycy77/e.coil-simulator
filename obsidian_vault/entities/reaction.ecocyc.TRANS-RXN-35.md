---
entity_id: "reaction.ecocyc.TRANS-RXN-35"
entity_type: "reaction"
name: "D-glucuronate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-35"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-glucuronate:proton symport

`reaction.ecocyc.TRANS-RXN-35`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-35`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GLUCURONATE + PROTON -> GLUCURONATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: GLUCURONATE + PROTON -> GLUCURONATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by exuT (protein.P0AA78). Substrates: H+ (molecule.C00080), D-Glucuronate (molecule.C00191). Products: H+ (molecule.C00080), D-Glucuronate (molecule.C00191).

## Annotation

GLUCURONATE + PROTON -> GLUCURONATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AA78|protein.P0AA78]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00191|molecule.C00191]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00191|molecule.C00191]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-35`

## Notes

GLUCURONATE + PROTON -> GLUCURONATE + PROTON; direction=REVERSIBLE
