---
entity_id: "reaction.ecocyc.3.4.21.102-RXN"
entity_type: "reaction"
name: "3.4.21.102-RXN"
source_database: "EcoCyc"
source_id: "3.4.21.102-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Tail-specific protease"
  - "Protease Re"
  - "Photosystem II D1 protein processing peptidase"
---

# 3.4.21.102-RXN

`reaction.ecocyc.3.4.21.102-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.21.102-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by prc (protein.P23865). Substrates: H2O (molecule.C00001).

## Annotation

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P23865|protein.P23865]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5541|molecule.ecocyc.CPD-5541]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-6301|molecule.ecocyc.CPD-6301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE|molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.4.21.102-RXN`

## Notes

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
