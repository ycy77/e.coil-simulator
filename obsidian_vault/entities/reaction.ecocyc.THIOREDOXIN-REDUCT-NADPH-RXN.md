---
entity_id: "reaction.ecocyc.THIOREDOXIN-REDUCT-NADPH-RXN"
entity_type: "reaction"
name: "THIOREDOXIN-REDUCT-NADPH-RXN"
source_database: "EcoCyc"
source_id: "THIOREDOXIN-REDUCT-NADPH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THIOREDOXIN-REDUCT-NADPH-RXN

`reaction.ecocyc.THIOREDOXIN-REDUCT-NADPH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction facilitates the reduction of disulfide bonds by pyridine nucleotides via the flavin moiety. EcoCyc reaction equation: Red-Thioredoxin + NADP -> Ox-Thioredoxin + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction facilitates the reduction of disulfide bonds by pyridine nucleotides via the flavin moiety.

## Biological Role

Catalyzed by thioredoxin reductase (complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.THIOREDOX-PWY` thioredoxin pathway (NADPH) (EcoCyc)

## Annotation

This reaction facilitates the reduction of disulfide bonds by pyridine nucleotides via the flavin moiety.

## Pathways

- `ecocyc.THIOREDOX-PWY` thioredoxin pathway (NADPH) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX|complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7388|molecule.ecocyc.CPD-7388]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-763|molecule.ecocyc.CPD-763]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1355|molecule.ecocyc.CPD0-1355]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN`

## Notes

Red-Thioredoxin + NADP -> Ox-Thioredoxin + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
