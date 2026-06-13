---
entity_id: "reaction.ecocyc.TRANS-RXN0-181"
entity_type: "reaction"
name: "protein translocation"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-181"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# protein translocation

`reaction.ecocyc.TRANS-RXN0-181`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-181`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

a-Tat-pathway-protein-substrate -> a-Tat-pathway-protein-substrate; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-Tat-pathway-protein-substrate -> a-Tat-pathway-protein-substrate; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by twin arginine protein translocation system (complex.ecocyc.TATABCE-CPLX).

## Annotation

a-Tat-pathway-protein-substrate -> a-Tat-pathway-protein-substrate; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.TATABCE-CPLX|complex.ecocyc.TATABCE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `represses` <-- [[molecule.ecocyc.CPD-20898|molecule.ecocyc.CPD-20898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-20899|molecule.ecocyc.CPD-20899]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-181`

## Notes

a-Tat-pathway-protein-substrate -> a-Tat-pathway-protein-substrate; direction=PHYSIOL-LEFT-TO-RIGHT
