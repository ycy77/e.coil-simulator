---
entity_id: "reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "LYSINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "LYSINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "LYSYL-TRNA SYNTHETASE"
---

# LYSINE--TRNA-LIGASE-RXN

`reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LYSINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LYS + LYS-tRNAs + ATP -> Charged-LYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LYS + LYS-tRNAs + ATP -> Charged-LYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine—tRNA ligase, constitutive (complex.ecocyc.LYSS-CPLX), lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX). Substrates: ATP (molecule.C00002), L-Lysine (molecule.C00047). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

LYS + LYS-tRNAs + ATP -> Charged-LYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.LYSS-CPLX|complex.ecocyc.LYSS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LYSINE--TRNA-LIGASE-RXN`

## Notes

LYS + LYS-tRNAs + ATP -> Charged-LYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
