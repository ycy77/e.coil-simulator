---
entity_id: "reaction.ecocyc.RXN-17780"
entity_type: "reaction"
name: "RXN-17780"
source_database: "EcoCyc"
source_id: "RXN-17780"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17780

`reaction.ecocyc.RXN-17780`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17780`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19168 -> CPD-19170 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-19168 -> CPD-19170 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: (S)-3-hydroxy-(7Z)-hexadecenoyl-CoA (molecule.ecocyc.CPD-19168). Products: H2O (molecule.C00001), (2E,7Z)-hexadec-2,7-dienoyl-CoA (molecule.ecocyc.CPD-19170).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-19168 -> CPD-19170 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19170|molecule.ecocyc.CPD-19170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19168|molecule.ecocyc.CPD-19168]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17780`

## Notes

CPD-19168 -> CPD-19170 + WATER; direction=REVERSIBLE
