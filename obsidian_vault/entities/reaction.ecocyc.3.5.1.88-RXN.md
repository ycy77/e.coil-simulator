---
entity_id: "reaction.ecocyc.3.5.1.88-RXN"
entity_type: "reaction"
name: "3.5.1.88-RXN"
source_database: "EcoCyc"
source_id: "3.5.1.88-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.5.1.88-RXN

`reaction.ecocyc.3.5.1.88-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.5.1.88-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMYL-L-METHIONYL-PEPTIDE + WATER -> METHIONYL-PEPTIDE + FORMATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMYL-L-METHIONYL-PEPTIDE + WATER -> METHIONYL-PEPTIDE + FORMATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by def (protein.P0A6K3). Substrates: H2O (molecule.C00001), a [protein] N-terminal-formyl-L-methionine (molecule.ecocyc.FORMYL-L-METHIONYL-PEPTIDE). Products: Formate (molecule.C00058), an N-terminal L-methionyl-[protein] (molecule.ecocyc.METHIONYL-PEPTIDE).

## Annotation

FORMYL-L-METHIONYL-PEPTIDE + WATER -> METHIONYL-PEPTIDE + FORMATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[protein.P0A6K3|protein.P0A6K3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.METHIONYL-PEPTIDE|molecule.ecocyc.METHIONYL-PEPTIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FORMYL-L-METHIONYL-PEPTIDE|molecule.ecocyc.FORMYL-L-METHIONYL-PEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06802|molecule.C06802]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1358|molecule.ecocyc.CPD0-1358]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1359|molecule.ecocyc.CPD0-1359]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1360|molecule.ecocyc.CPD0-1360]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1708|molecule.ecocyc.CPD0-1708]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.5.1.88-RXN`

## Notes

FORMYL-L-METHIONYL-PEPTIDE + WATER -> METHIONYL-PEPTIDE + FORMATE; direction=PHYSIOL-LEFT-TO-RIGHT
