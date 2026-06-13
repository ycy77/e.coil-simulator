---
entity_id: "reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN"
entity_type: "reaction"
name: "325-BISPHOSPHATE-NUCLEOTIDASE-RXN"
source_database: "EcoCyc"
source_id: "325-BISPHOSPHATE-NUCLEOTIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Phosphoadenylate 3'-nucleotidase"
  - "3'(2'),5'-bisphosphonucleoside 3'(2')-phosphohydrolase"
  - "3'-phosphoadenylylsulfate 3'-phosphatase"
  - "DPNPase"
---

# 325-BISPHOSPHATE-NUCLEOTIDASE-RXN

`reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:325-BISPHOSPHATE-NUCLEOTIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-5-ADP + WATER -> Pi + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-5-ADP + WATER -> Pi + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysQ (protein.P22255). Substrates: H2O (molecule.C00001), Adenosine 3',5'-bisphosphate (molecule.C00054). Products: AMP (molecule.C00020), phosphate (molecule.ecocyc.Pi).

## Annotation

3-5-ADP + WATER -> Pi + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P22255|protein.P22255]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00054|molecule.C00054]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:325-BISPHOSPHATE-NUCLEOTIDASE-RXN`

## Notes

3-5-ADP + WATER -> Pi + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
