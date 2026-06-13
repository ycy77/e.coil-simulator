---
entity_id: "reaction.ecocyc.RXN-17790"
entity_type: "reaction"
name: "RXN-17790"
source_database: "EcoCyc"
source_id: "RXN-17790"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17790

`reaction.ecocyc.RXN-17790`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17790`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19155 + NAD -> CPD-19158 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-19155 + NAD -> CPD-19158 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: NAD+ (molecule.C00003), (S)-3-hydroxy-(9Z)-hexadecenoyl-CoA (molecule.ecocyc.CPD-19155). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-oxo-(9Z)-hexadecenoyl-CoA (molecule.ecocyc.CPD-19158).

## Annotation

CPD-19155 + NAD -> CPD-19158 + NADH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19158|molecule.ecocyc.CPD-19158]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19155|molecule.ecocyc.CPD-19155]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17790`

## Notes

CPD-19155 + NAD -> CPD-19158 + NADH + PROTON; direction=REVERSIBLE
