---
entity_id: "reaction.ecocyc.ARGININE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "ARGININE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "ARGININE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "ARGINYL-TRNA SYNTHETASE"
---

# ARGININE--TRNA-LIGASE-RXN

`reaction.ecocyc.ARGININE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ARGININE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ARG-tRNAs + ARG + ATP -> Charged-ARG-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ARG-tRNAs + ARG + ATP -> Charged-ARG-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by argS (protein.P11875). Substrates: ATP (molecule.C00002), L-Arginine (molecule.C00062). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

ARG-tRNAs + ARG + ATP -> Charged-ARG-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P11875|protein.P11875]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CANAVANINE|molecule.ecocyc.CANAVANINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HOMOARGININE|molecule.ecocyc.HOMOARGININE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ARGININE--TRNA-LIGASE-RXN`

## Notes

ARG-tRNAs + ARG + ATP -> Charged-ARG-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
