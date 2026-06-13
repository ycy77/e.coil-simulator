---
entity_id: "reaction.ecocyc.ISOLEUCINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "ISOLEUCINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "ISOLEUCINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "ISOLEUCYL-TRNA SYNTHETASE"
---

# ISOLEUCINE--TRNA-LIGASE-RXN

`reaction.ecocyc.ISOLEUCINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ISOLEUCINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ILE-tRNAs + ILE + ATP -> Charged-ILE-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ILE-tRNAs + ILE + ATP -> Charged-ILE-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ileS (protein.P00956). Substrates: ATP (molecule.C00002), L-Isoleucine (molecule.C00407). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

ILE-tRNAs + ILE + ATP -> Charged-ILE-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P00956|protein.P00956]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1234|molecule.ecocyc.CPD0-1234]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1357|molecule.ecocyc.CPD0-1357]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2581|molecule.ecocyc.CPD0-2581]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ISOLEUCINE--TRNA-LIGASE-RXN`

## Notes

ILE-tRNAs + ILE + ATP -> Charged-ILE-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
