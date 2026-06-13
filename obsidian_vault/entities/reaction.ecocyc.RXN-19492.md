---
entity_id: "reaction.ecocyc.RXN-19492"
entity_type: "reaction"
name: "RXN-19492"
source_database: "EcoCyc"
source_id: "RXN-19492"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19492

`reaction.ecocyc.RXN-19492`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19492`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-6761 -> OXOPENTENOATE; direction=REVERSIBLE EcoCyc reaction equation: CPD-6761 -> OXOPENTENOATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by tautomerase PptA (complex.ecocyc.CPLX0-902). Substrates: (2E)-2-hydroxypenta-2,4-dienoate (molecule.ecocyc.CPD-6761). Products: 2-Hydroxy-2,4-pentadienoate (molecule.C00596).

## Annotation

CPD-6761 -> OXOPENTENOATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-902|complex.ecocyc.CPLX0-902]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00596|molecule.C00596]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-6761|molecule.ecocyc.CPD-6761]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00180|molecule.C00180]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2682|molecule.ecocyc.CPD0-2682]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HEPES|molecule.ecocyc.HEPES]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-19492`

## Notes

CPD-6761 -> OXOPENTENOATE; direction=REVERSIBLE
