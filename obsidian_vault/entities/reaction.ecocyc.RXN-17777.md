---
entity_id: "reaction.ecocyc.RXN-17777"
entity_type: "reaction"
name: "RXN-17777"
source_database: "EcoCyc"
source_id: "RXN-17777"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17777

`reaction.ecocyc.RXN-17777`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17777`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + CPD-19171 -> NADH + PROTON + CPD-19169; direction=REVERSIBLE EcoCyc reaction equation: NAD + CPD-19171 -> NADH + PROTON + CPD-19169; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: NAD+ (molecule.C00003), (S)-3-hydroxy-(9Z)-octadecenoyl-CoA (molecule.ecocyc.CPD-19171). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-oxo-(9Z)-octadecenoyl-CoA (molecule.ecocyc.CPD-19169).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

NAD + CPD-19171 -> NADH + PROTON + CPD-19169; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19169|molecule.ecocyc.CPD-19169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19171|molecule.ecocyc.CPD-19171]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17777`

## Notes

NAD + CPD-19171 -> NADH + PROTON + CPD-19169; direction=REVERSIBLE
