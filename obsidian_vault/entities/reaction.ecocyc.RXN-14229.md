---
entity_id: "reaction.ecocyc.RXN-14229"
entity_type: "reaction"
name: "RXN-14229"
source_database: "EcoCyc"
source_id: "RXN-14229"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14229

`reaction.ecocyc.RXN-14229`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14229`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-196 + ETF-Oxidized + PROTON -> CPD0-2108 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-196 + ETF-Oxidized + PROTON -> CPD0-2108 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), Octanoyl-CoA (molecule.C01944). Products: trans-Oct-2-enoyl-CoA (molecule.C05276).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-196 + ETF-Oxidized + PROTON -> CPD0-2108 + ETF-Reduced; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C05276|molecule.C05276]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01944|molecule.C01944]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14229`

## Notes

CPD-196 + ETF-Oxidized + PROTON -> CPD0-2108 + ETF-Reduced; direction=REVERSIBLE
