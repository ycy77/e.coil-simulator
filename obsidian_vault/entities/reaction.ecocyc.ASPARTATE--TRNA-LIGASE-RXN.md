---
entity_id: "reaction.ecocyc.ASPARTATE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "ASPARTATE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "ASPARTATE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "ASPARTYL-TRNA SYNTHETASE"
---

# ASPARTATE--TRNA-LIGASE-RXN

`reaction.ecocyc.ASPARTATE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPARTATE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ASP-tRNAs + L-ASPARTATE + ATP -> Charged-ASP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ASP-tRNAs + L-ASPARTATE + ATP -> Charged-ASP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aspartate—tRNA ligase (complex.ecocyc.ASPS-CPLX). Substrates: ATP (molecule.C00002), L-Aspartate (molecule.C00049). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

ASP-tRNAs + L-ASPARTATE + ATP -> Charged-ASP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ASPS-CPLX|complex.ecocyc.ASPS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-914|molecule.ecocyc.CPD0-914]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-915|molecule.ecocyc.CPD0-915]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-916|molecule.ecocyc.CPD0-916]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPARTATE--TRNA-LIGASE-RXN`

## Notes

ASP-tRNAs + L-ASPARTATE + ATP -> Charged-ASP-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
