---
entity_id: "reaction.ecocyc.RXN-19959"
entity_type: "reaction"
name: "RXN-19959"
source_database: "EcoCyc"
source_id: "RXN-19959"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19959

`reaction.ecocyc.RXN-19959`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19959`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Medium-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Medium-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Medium-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Medium-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fadK (protein.P38135). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), a medium-chain 2,3,4-saturated fatty acid (molecule.ecocyc.Medium-Chain-234-Saturated-Fatty-Acids). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), a medium-chain 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Medium-Chain-234-Saturated-acyl-CoAs).

## Annotation

Medium-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Medium-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P38135|protein.P38135]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Medium-Chain-234-Saturated-acyl-CoAs|molecule.ecocyc.Medium-Chain-234-Saturated-acyl-CoAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Medium-Chain-234-Saturated-Fatty-Acids|molecule.ecocyc.Medium-Chain-234-Saturated-Fatty-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19959`

## Notes

Medium-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Medium-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
