---
entity_id: "reaction.ecocyc.RXN-12490"
entity_type: "reaction"
name: "RXN-12490"
source_database: "EcoCyc"
source_id: "RXN-12490"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12490

`reaction.ecocyc.RXN-12490`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12490`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2244 + NAD -> CPD0-2123 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2244 + NAD -> CPD0-2123 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: NAD+ (molecule.C00003), (S)-Hydroxydecanoyl-CoA (molecule.C05264). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Oxodecanoyl-CoA (molecule.C05265).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-2244 + NAD -> CPD0-2123 + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05265|molecule.C05265]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05264|molecule.C05264]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12490`

## Notes

CPD0-2244 + NAD -> CPD0-2123 + NADH + PROTON; direction=REVERSIBLE
