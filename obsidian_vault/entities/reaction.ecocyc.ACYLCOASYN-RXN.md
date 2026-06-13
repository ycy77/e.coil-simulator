---
entity_id: "reaction.ecocyc.ACYLCOASYN-RXN"
entity_type: "reaction"
name: "2,3,4-saturated fatty acyl-CoA synthetase"
source_database: "EcoCyc"
source_id: "ACYLCOASYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2,3,4-saturated fatty acyl-CoA synthetase

`reaction.ecocyc.ACYLCOASYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACYLCOASYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the first step of β-oxidation of fatty acids. R= saturated aliphatic chain. EcoCyc reaction equation: CPD66-39 + CO-A + ATP -> Saturated-Fatty-Acyl-CoA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the first step of β-oxidation of fatty acids. R= saturated aliphatic chain.

## Biological Role

Substrates: ATP (molecule.C00002), CoA (molecule.C00010), a 2,3,4-saturated fatty acid (molecule.ecocyc.CPD66-39). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), a 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Saturated-Fatty-Acyl-CoA).

## Enriched Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Annotation

This reaction is the first step of β-oxidation of fatty acids. R= saturated aliphatic chain.

## Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD66-39|molecule.ecocyc.CPD66-39]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACYLCOASYN-RXN`

## Notes

CPD66-39 + CO-A + ATP -> Saturated-Fatty-Acyl-CoA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
