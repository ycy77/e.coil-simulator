---
entity_id: "reaction.ecocyc.RXN-15140"
entity_type: "reaction"
name: "RXN-15140"
source_database: "EcoCyc"
source_id: "RXN-15140"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15140

`reaction.ecocyc.RXN-15140`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15140`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEOXYADENOSINE + CPD-12377 -> CPD-16020 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DEOXYADENOSINE + CPD-12377 -> CPD-16020 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Deoxyadenosine (molecule.C00559), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: H2O (molecule.C00001), 2-oxo-2'-deoxyadenosine (molecule.ecocyc.CPD-16020).

## Annotation

DEOXYADENOSINE + CPD-12377 -> CPD-16020 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16020|molecule.ecocyc.CPD-16020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00559|molecule.C00559]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15140`

## Notes

DEOXYADENOSINE + CPD-12377 -> CPD-16020 + WATER; direction=LEFT-TO-RIGHT
