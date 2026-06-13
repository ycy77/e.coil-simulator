---
entity_id: "reaction.ecocyc.RXN-14278"
entity_type: "reaction"
name: "hexanoyl-CoA dehydrogenase"
source_database: "EcoCyc"
source_id: "RXN-14278"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hexanoyl-CoA dehydrogenase

`reaction.ecocyc.RXN-14278`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14278`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HEXANOYL-COA + ETF-Oxidized + PROTON -> CPD0-2121 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: HEXANOYL-COA + ETF-Oxidized + PROTON -> CPD0-2121 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), Hexanoyl-CoA (molecule.C05270). Products: trans-Hex-2-enoyl-CoA (molecule.C05271).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

HEXANOYL-COA + ETF-Oxidized + PROTON -> CPD0-2121 + ETF-Reduced; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C05271|molecule.C05271]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05270|molecule.C05270]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14278`

## Notes

HEXANOYL-COA + ETF-Oxidized + PROTON -> CPD0-2121 + ETF-Reduced; direction=REVERSIBLE
