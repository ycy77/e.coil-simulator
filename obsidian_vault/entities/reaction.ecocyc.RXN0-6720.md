---
entity_id: "reaction.ecocyc.RXN0-6720"
entity_type: "reaction"
name: "RXN0-6720"
source_database: "EcoCyc"
source_id: "RXN0-6720"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6720

`reaction.ecocyc.RXN0-6720`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6720`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2467 + WATER -> CPD0-2468; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2467 + WATER -> CPD0-2468; direction=REVERSIBLE.

## Biological Role

Catalyzed by lsrG (protein.P64461). Substrates: H2O (molecule.C00001), 3-hydroxy-2,4-dioxopentyl phosphate (molecule.ecocyc.CPD0-2467). Products: 3,4,4-trihydroxy-5-phosphooxypentan-2-one (molecule.ecocyc.CPD0-2468).

## Annotation

CPD0-2467 + WATER -> CPD0-2468; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P64461|protein.P64461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2468|molecule.ecocyc.CPD0-2468]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2467|molecule.ecocyc.CPD0-2467]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6720`

## Notes

CPD0-2467 + WATER -> CPD0-2468; direction=REVERSIBLE
