---
entity_id: "reaction.ecocyc.TRYPTOPHAN--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "TRYPTOPHAN--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "TRYPTOPHAN--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "TRYPTOPHANYL-TRNA SYNTHETASE"
---

# TRYPTOPHAN--TRNA-LIGASE-RXN

`reaction.ecocyc.TRYPTOPHAN--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRYPTOPHAN--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TRP + TRP-tRNAs + ATP -> Charged-TRP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TRP + TRP-tRNAs + ATP -> Charged-TRP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tryptophan—tRNA ligase (complex.ecocyc.TRPS-CPLX). Substrates: ATP (molecule.C00002), L-Tryptophan (molecule.C00078). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

TRP + TRP-tRNAs + ATP -> Charged-TRP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.TRPS-CPLX|complex.ecocyc.TRPS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1480|molecule.ecocyc.CPD0-1480]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-920|molecule.ecocyc.CPD0-920]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRYPTOPHAN--TRNA-LIGASE-RXN`

## Notes

TRP + TRP-tRNAs + ATP -> Charged-TRP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
