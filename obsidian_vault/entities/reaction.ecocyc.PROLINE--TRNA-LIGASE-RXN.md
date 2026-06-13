---
entity_id: "reaction.ecocyc.PROLINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "PROLINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "PROLINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PROLYL-TRNA SYNTHETASE"
---

# PROLINE--TRNA-LIGASE-RXN

`reaction.ecocyc.PROLINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROLINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PRO-tRNAs + PRO + ATP -> Charged-PRO-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PRO-tRNAs + PRO + ATP -> Charged-PRO-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by proline—tRNA ligase (complex.ecocyc.PROS-CPLX). Substrates: ATP (molecule.C00002), L-Proline (molecule.C00148). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

PRO-tRNAs + PRO + ATP -> Charged-PRO-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.PROS-CPLX|complex.ecocyc.PROS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROLINE--TRNA-LIGASE-RXN`

## Notes

PRO-tRNAs + PRO + ATP -> Charged-PRO-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
