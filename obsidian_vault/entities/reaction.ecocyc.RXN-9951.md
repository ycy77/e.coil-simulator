---
entity_id: "reaction.ecocyc.RXN-9951"
entity_type: "reaction"
name: "isocitrate dehydrogenase (NADP+)"
source_database: "EcoCyc"
source_id: "RXN-9951"
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

# isocitrate dehydrogenase (NADP+)

`reaction.ecocyc.RXN-9951`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9951`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THREO-DS-ISO-CITRATE + NADP -> OXALO-SUCCINATE + NADPH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: THREO-DS-ISO-CITRATE + NADP -> OXALO-SUCCINATE + NADPH + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: NADP+ (molecule.C00006), D-threo-isocitrate (molecule.ecocyc.THREO-DS-ISO-CITRATE). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Oxalosuccinate (molecule.C05379).

## Annotation

THREO-DS-ISO-CITRATE + NADP -> OXALO-SUCCINATE + NADPH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05379|molecule.C05379]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.THREO-DS-ISO-CITRATE|molecule.ecocyc.THREO-DS-ISO-CITRATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9951`

## Notes

THREO-DS-ISO-CITRATE + NADP -> OXALO-SUCCINATE + NADPH + PROTON; direction=REVERSIBLE
