---
entity_id: "reaction.ecocyc.RXN-17785"
entity_type: "reaction"
name: "RXN-17785"
source_database: "EcoCyc"
source_id: "RXN-17785"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17785

`reaction.ecocyc.RXN-17785`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17785`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19159 -> CPD-19163 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-19159 -> CPD-19163 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: (S)-3-hydroxy-(11Z)-octadecenoyl-CoA (molecule.ecocyc.CPD-19159). Products: H2O (molecule.C00001), (2E,11Z)-octadec-2,11-enoyl-CoA (molecule.ecocyc.CPD-19163).

## Annotation

CPD-19159 -> CPD-19163 + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19163|molecule.ecocyc.CPD-19163]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19159|molecule.ecocyc.CPD-19159]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17785`

## Notes

CPD-19159 -> CPD-19163 + WATER; direction=REVERSIBLE
