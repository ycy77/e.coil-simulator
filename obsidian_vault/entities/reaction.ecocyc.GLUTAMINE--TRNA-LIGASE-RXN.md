---
entity_id: "reaction.ecocyc.GLUTAMINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "GLUTAMINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "GLUTAMINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GLUTAMINYL-TRNA SYNTHETASE"
---

# GLUTAMINE--TRNA-LIGASE-RXN

`reaction.ecocyc.GLUTAMINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTAMINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLN-tRNAs + GLN + ATP -> Charged-GLN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLN-tRNAs + GLN + ATP -> Charged-GLN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glnS (protein.P00962). Substrates: ATP (molecule.C00002), L-Glutamine (molecule.C00064). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

GLN-tRNAs + GLN + ATP -> Charged-GLN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00962|protein.P00962]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1086|molecule.ecocyc.CPD0-1086]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTAMINE--TRNA-LIGASE-RXN`

## Notes

GLN-tRNAs + GLN + ATP -> Charged-GLN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
