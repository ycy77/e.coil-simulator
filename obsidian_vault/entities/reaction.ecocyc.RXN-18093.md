---
entity_id: "reaction.ecocyc.RXN-18093"
entity_type: "reaction"
name: "RXN-18093"
source_database: "EcoCyc"
source_id: "RXN-18093"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18093

`reaction.ecocyc.RXN-18093`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18093`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-9385 + GLYCYLGLYCINE -> 4-NITROANILINE + CPD-19395; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9385 + GLYCYLGLYCINE -> 4-NITROANILINE + CPD-19395; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutathione hydrolase (complex.ecocyc.CPLX0-7885). Substrates: γ-glutamyl-p-nitroanilide (molecule.ecocyc.CPD-9385), glycyl-glycine (molecule.ecocyc.GLYCYLGLYCINE). Products: 4-nitroaniline (molecule.ecocyc.4-NITROANILINE), γ-L-glutamyl-glycylglycine (molecule.ecocyc.CPD-19395).

## Annotation

CPD-9385 + GLYCYLGLYCINE -> 4-NITROANILINE + CPD-19395; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7885|complex.ecocyc.CPLX0-7885]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.4-NITROANILINE|molecule.ecocyc.4-NITROANILINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19395|molecule.ecocyc.CPD-19395]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9385|molecule.ecocyc.CPD-9385]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLYCYLGLYCINE|molecule.ecocyc.GLYCYLGLYCINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18093`

## Notes

CPD-9385 + GLYCYLGLYCINE -> 4-NITROANILINE + CPD-19395; direction=LEFT-TO-RIGHT
