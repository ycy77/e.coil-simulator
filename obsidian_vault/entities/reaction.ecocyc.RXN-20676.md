---
entity_id: "reaction.ecocyc.RXN-20676"
entity_type: "reaction"
name: "RXN-20676"
source_database: "EcoCyc"
source_id: "RXN-20676"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20676

`reaction.ecocyc.RXN-20676`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20676`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2107 + NAD -> CPD0-2105 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2107 + NAD -> CPD0-2105 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: NAD+ (molecule.C00003), (S)-3-Hydroxydodecanoyl-CoA (molecule.C05262). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Oxododecanoyl-CoA (molecule.C05263).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-2107 + NAD -> CPD0-2105 + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05263|molecule.C05263]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05262|molecule.C05262]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20676`

## Notes

CPD0-2107 + NAD -> CPD0-2105 + NADH + PROTON; direction=REVERSIBLE
