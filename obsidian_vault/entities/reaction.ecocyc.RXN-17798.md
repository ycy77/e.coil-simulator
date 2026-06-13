---
entity_id: "reaction.ecocyc.RXN-17798"
entity_type: "reaction"
name: "RXN-17798"
source_database: "EcoCyc"
source_id: "RXN-17798"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17798

`reaction.ecocyc.RXN-17798`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17798`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19151 + NAD -> CPD-19153 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-19151 + NAD -> CPD-19153 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: NAD+ (molecule.C00003), (S)-3-hydroxy-(5Z)-dodecenoyl-CoA (molecule.ecocyc.CPD-19151). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-oxo-(5Z)-dodecenoyl-CoA (molecule.ecocyc.CPD-19153).

## Annotation

CPD-19151 + NAD -> CPD-19153 + NADH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19153|molecule.ecocyc.CPD-19153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19151|molecule.ecocyc.CPD-19151]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17798`

## Notes

CPD-19151 + NAD -> CPD-19153 + NADH + PROTON; direction=REVERSIBLE
