---
entity_id: "reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "TYROSINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "TYROSINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "TYROSYL-TRNA SYNTHETASE"
---

# TYROSINE--TRNA-LIGASE-RXN

`reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TYROSINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TYR-tRNAs + TYR + ATP -> Charged-TYR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TYR-tRNAs + TYR + ATP -> Charged-TYR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tyrosine—tRNA ligase (complex.ecocyc.TYRS-CPLX). Substrates: ATP (molecule.C00002), L-Tyrosine (molecule.C00082). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

TYR-tRNAs + TYR + ATP -> Charged-TYR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.TYRS-CPLX|complex.ecocyc.TYRS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TYROSINE--TRNA-LIGASE-RXN`

## Notes

TYR-tRNAs + TYR + ATP -> Charged-TYR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
