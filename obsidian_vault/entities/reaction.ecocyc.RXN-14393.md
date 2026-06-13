---
entity_id: "reaction.ecocyc.RXN-14393"
entity_type: "reaction"
name: "RXN-14393"
source_database: "EcoCyc"
source_id: "RXN-14393"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14393

`reaction.ecocyc.RXN-14393`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14393`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1163 + NAD -> CPD-15244 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1163 + NAD -> CPD-15244 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: NAD+ (molecule.C00003), (S)-3-hydroxy-(5Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD0-1163). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-oxo-(5Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-15244).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-1163 + NAD -> CPD-15244 + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15244|molecule.ecocyc.CPD-15244]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1163|molecule.ecocyc.CPD0-1163]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14393`

## Notes

CPD0-1163 + NAD -> CPD-15244 + NADH + PROTON; direction=REVERSIBLE
