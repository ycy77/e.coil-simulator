---
entity_id: "reaction.ecocyc.RXN-8642"
entity_type: "reaction"
name: "isocitrate:NADP+ oxidoreductase (decarboxylating)"
source_database: "EcoCyc"
source_id: "RXN-8642"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "oxalosuccinate decarboxylase"
  - "oxalsuccinic decarboxylase"
  - "isocitrate (NADP) dehydrogenase"
  - "isocitrate (nicotinamide adenine dinucleotide phosphate) dehydrogenase"
  - "NADP-specific isocitrate dehydrogenase"
  - "NADP-linked isocitrate dehydrogenase"
  - "NADP-dependent isocitrate dehydrogenase"
  - "NADP isocitric dehydrogenase"
  - "isocitrate dehydrogenase (NADP-dependent)"
  - "NADP-dependent isocitric dehydrogenase"
  - "triphosphopyridine nucleotide-linked isocitrate dehydrogenase-oxalosuccinate carboxylase"
  - "NADP<small><sup>+</sup></small>-linked isocitrate dehydrogenase"
  - "IDH (ambiguous)"
  - "dual-cofactor-specific isocitrate dehydrogenase"
  - "NADP<small><sup>+</sup></small>-ICDH"
  - "NADP<small><sup>+</sup></small>-IDH"
  - "IDP"
  - "IDP1"
  - "IDP2"
  - "IDP3"
---

# isocitrate:NADP+ oxidoreductase (decarboxylating)

`reaction.ecocyc.RXN-8642`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8642`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OXALO-SUCCINATE + PROTON -> 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE EcoCyc reaction equation: OXALO-SUCCINATE + PROTON -> 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), Oxalosuccinate (molecule.C05379). Products: CO2 (molecule.C00011), 2-Oxoglutarate (molecule.C00026).

## Annotation

OXALO-SUCCINATE + PROTON -> 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05379|molecule.C05379]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8642`

## Notes

OXALO-SUCCINATE + PROTON -> 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE
