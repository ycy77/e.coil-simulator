---
entity_id: "reaction.ecocyc.RXN-18678"
entity_type: "reaction"
name: "RXN-18678"
source_database: "EcoCyc"
source_id: "RXN-18678"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18678

`reaction.ecocyc.RXN-18678`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18678`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

signal-peptide + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: signal-peptide + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rseP (protein.P0AEH1). Substrates: H2O (molecule.C00001), a signal peptide (molecule.ecocyc.signal-peptide).

## Annotation

signal-peptide + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AEH1|protein.P0AEH1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.signal-peptide|molecule.ecocyc.signal-peptide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18678`

## Notes

signal-peptide + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT
