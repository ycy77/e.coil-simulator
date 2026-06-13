---
entity_id: "reaction.ecocyc.THREONINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "THREONINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "THREONINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "THREONYL-TRNA SYNTHETASE"
---

# THREONINE--TRNA-LIGASE-RXN

`reaction.ecocyc.THREONINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THREONINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THR-tRNAs + THR + ATP -> Charged-THR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THR-tRNAs + THR + ATP -> Charged-THR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by threonine—tRNA ligase (complex.ecocyc.THRS-CPLX). Substrates: ATP (molecule.C00002), L-Threonine (molecule.C00188). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

THR-tRNAs + THR + ATP -> Charged-THR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.THRS-CPLX|complex.ecocyc.THRS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1348|molecule.ecocyc.CPD0-1348]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2689|molecule.ecocyc.CPD0-2689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THREONINE--TRNA-LIGASE-RXN`

## Notes

THR-tRNAs + THR + ATP -> Charged-THR-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
