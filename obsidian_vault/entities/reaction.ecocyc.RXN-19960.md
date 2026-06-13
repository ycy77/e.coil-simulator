---
entity_id: "reaction.ecocyc.RXN-19960"
entity_type: "reaction"
name: "RXN-19960"
source_database: "EcoCyc"
source_id: "RXN-19960"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19960

`reaction.ecocyc.RXN-19960`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19960`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Long-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Long-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Long-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Long-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by long-chain-fatty-acid—CoA ligase (complex.ecocyc.ACYLCOASYN-CPLX). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), a long-chain 2,3,4-saturated fatty acid (molecule.ecocyc.Long-Chain-234-Saturated-Fatty-Acids). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), a long-chain 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Long-Chain-234-Saturated-acyl-CoAs).

## Annotation

Long-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Long-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ACYLCOASYN-CPLX|complex.ecocyc.ACYLCOASYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Long-Chain-234-Saturated-acyl-CoAs|molecule.ecocyc.Long-Chain-234-Saturated-acyl-CoAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Long-Chain-234-Saturated-Fatty-Acids|molecule.ecocyc.Long-Chain-234-Saturated-Fatty-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1385|molecule.ecocyc.CPD0-1385]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HSCN|molecule.ecocyc.HSCN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-19960`

## Notes

Long-Chain-234-Saturated-Fatty-Acids + CO-A + ATP -> Long-Chain-234-Saturated-acyl-CoAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
