---
entity_id: "reaction.ecocyc.3.4.11.18-RXN"
entity_type: "reaction"
name: "3.4.11.18-RXN"
source_database: "EcoCyc"
source_id: "3.4.11.18-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Methionine aminopeptidase"
  - "Peptidase M"
---

# 3.4.11.18-RXN

`reaction.ecocyc.3.4.11.18-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.11.18-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-With-N-Terminal-Met + WATER -> MET + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-With-N-Terminal-Met + WATER -> MET + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by map (protein.P0AE18). Substrates: H2O (molecule.C00001). Products: L-Methionine (molecule.C00073).

## Annotation

Protein-With-N-Terminal-Met + WATER -> MET + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AE18|protein.P0AE18]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.5-IODOPENTAPHOSPHONATE|molecule.ecocyc.5-IODOPENTAPHOSPHONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1436|molecule.ecocyc.CPD0-1436]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2595|molecule.ecocyc.CPD0-2595]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-QUINOLIN-8-YLMETHANESULFONAMI|molecule.ecocyc.N-QUINOLIN-8-YLMETHANESULFONAMI]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.THIABENDAZOLE|molecule.ecocyc.THIABENDAZOLE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.4.11.18-RXN`

## Notes

Protein-With-N-Terminal-Met + WATER -> MET + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
