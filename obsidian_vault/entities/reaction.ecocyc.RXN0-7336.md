---
entity_id: "reaction.ecocyc.RXN0-7336"
entity_type: "reaction"
name: "RXN0-7336"
source_database: "EcoCyc"
source_id: "RXN0-7336"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7336

`reaction.ecocyc.RXN0-7336`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7336`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction represents the autophosphorylation of sensor histidine kinase ArcB at histidine residue 292. EcoCyc reaction equation: ARCB-CPLX + ATP -> PHOSPHO-ARCB-HIS + ADP; direction=LEFT-TO-RIGHT. This reaction represents the autophosphorylation of sensor histidine kinase ArcB at histidine residue 292.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1505` ArcAB Two-Component Signal Transduction System, quinone dependent (EcoCyc)

## Annotation

This reaction represents the autophosphorylation of sensor histidine kinase ArcB at histidine residue 292.

## Pathways

- `ecocyc.PWY0-1505` ArcAB Two-Component Signal Transduction System, quinone dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions

## External IDs

- `EcoCyc:RXN0-7336`

## Notes

ARCB-CPLX + ATP -> PHOSPHO-ARCB-HIS + ADP; direction=LEFT-TO-RIGHT
