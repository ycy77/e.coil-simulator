---
entity_id: "reaction.ecocyc.ALANINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "ALANINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "ALANINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "ALANYL-TRNA SYNTHETASE"
---

# ALANINE--TRNA-LIGASE-RXN

`reaction.ecocyc.ALANINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALANINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ALA-tRNAs + L-ALPHA-ALANINE + ATP -> Charged-ALA-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ALA-tRNAs + L-ALPHA-ALANINE + ATP -> Charged-ALA-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alanine—tRNA ligase/DNA-binding transcriptional repressor (complex.ecocyc.ALAS-CPLX). Substrates: ATP (molecule.C00002), L-Alanine (molecule.C00041). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

ALA-tRNAs + L-ALPHA-ALANINE + ATP -> Charged-ALA-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALAS-CPLX|complex.ecocyc.ALAS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALANINE--TRNA-LIGASE-RXN`

## Notes

ALA-tRNAs + L-ALPHA-ALANINE + ATP -> Charged-ALA-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
