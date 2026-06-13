---
entity_id: "reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN"
entity_type: "reaction"
name: "RIBONUCLEOSIDE-DIP-REDUCTI-RXN"
source_database: "EcoCyc"
source_id: "RIBONUCLEOSIDE-DIP-REDUCTI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBONUCLEOSIDE-DIP-REDUCTI-RXN

`reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes deoxynucleoside diphosphates. Thioredoxin is the reductant cofactor and NADPH is the ultimate hydrogen donor. EcoCyc reaction equation: Ox-Thioredoxin + WATER + Deoxy-Ribonucleoside-Diphosphates -> Red-Thioredoxin + Ribonucleoside-Diphosphates; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction synthesizes deoxynucleoside diphosphates. Thioredoxin is the reductant cofactor and NADPH is the ultimate hydrogen donor.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 1 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX), ribonucleoside-diphosphate reductase 2 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX). Substrates: H2O (molecule.C00001), a 2'-deoxyribonucleoside 5'-diphosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Diphosphates). Products: a ribonucleoside diphosphate (molecule.ecocyc.Ribonucleoside-Diphosphates).

## Annotation

This reaction synthesizes deoxynucleoside diphosphates. Thioredoxin is the reductant cofactor and NADPH is the ultimate hydrogen donor.

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Ribonucleoside-Diphosphates|molecule.ecocyc.Ribonucleoside-Diphosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Diphosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Diphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00705|molecule.C00705]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1392|molecule.ecocyc.CPD0-1392]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1393|molecule.ecocyc.CPD0-1393]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1394|molecule.ecocyc.CPD0-1394]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1395|molecule.ecocyc.CPD0-1395]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTI-RXN`

## Notes

Ox-Thioredoxin + WATER + Deoxy-Ribonucleoside-Diphosphates -> Red-Thioredoxin + Ribonucleoside-Diphosphates; direction=PHYSIOL-RIGHT-TO-LEFT
