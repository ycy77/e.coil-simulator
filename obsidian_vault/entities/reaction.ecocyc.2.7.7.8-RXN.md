---
entity_id: "reaction.ecocyc.2.7.7.8-RXN"
entity_type: "reaction"
name: "2.7.7.8-RXN"
source_database: "EcoCyc"
source_id: "2.7.7.8-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "POLYNUCLEOTIDE PHOSPHORYLASE"
---

# 2.7.7.8-RXN

`reaction.ecocyc.2.7.7.8-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.7.8-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP, IDP, GDP, UDP AND CDP CAN ACT AS DONORS. EcoCyc reaction equation: ssRNA-Holder + Pi -> ssRNA-Holder + Nucleoside-Diphosphates; direction=REVERSIBLE. ADP, IDP, GDP, UDP AND CDP CAN ACT AS DONORS.

## Biological Role

Catalyzed by polynucleotide phosphorylase (complex.ecocyc.CPLX0-3521). Substrates: phosphate (molecule.ecocyc.Pi), a single-stranded RNA (molecule.ecocyc.ssRNA-Holder). Products: a nucleoside diphosphate (molecule.ecocyc.Nucleoside-Diphosphates), a single-stranded RNA (molecule.ecocyc.ssRNA-Holder).

## Annotation

ADP, IDP, GDP, UDP AND CDP CAN ACT AS DONORS.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3521|complex.ecocyc.CPLX0-3521]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Diphosphates|molecule.ecocyc.Nucleoside-Diphosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ssRNA-Holder|molecule.ecocyc.ssRNA-Holder]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ssRNA-Holder|molecule.ecocyc.ssRNA-Holder]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1601|molecule.ecocyc.CPD0-1601]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.7.7.8-RXN`

## Notes

ssRNA-Holder + Pi -> ssRNA-Holder + Nucleoside-Diphosphates; direction=REVERSIBLE
