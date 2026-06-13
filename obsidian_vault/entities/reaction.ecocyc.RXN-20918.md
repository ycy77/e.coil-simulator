---
entity_id: "reaction.ecocyc.RXN-20918"
entity_type: "reaction"
name: "RXN-20918"
source_database: "EcoCyc"
source_id: "RXN-20918"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20918

`reaction.ecocyc.RXN-20918`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20918`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations. EcoCyc reaction equation: CPD-17523 + KDO2-LIPID-A -> 2-Acylglycero-Phosphocholines + CPD-22536; direction=PHYSIOL-LEFT-TO-RIGHT. The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations.

## Biological Role

Catalyzed by pagP (protein.P37001). Substrates: KDO2-lipid A (molecule.C06026), a 1-palmitoyl-2-acyl-sn-glycero-3-phosphocholine (molecule.ecocyc.CPD-17523). Products: 2-Acyl-sn-glycero-3-phosphocholine (molecule.C04233), hepta-acylated Kdo2 lipid A (E. coli) (molecule.ecocyc.CPD-22536).

## Annotation

The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37001|protein.P37001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04233|molecule.C04233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22536|molecule.ecocyc.CPD-22536]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06026|molecule.C06026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17523|molecule.ecocyc.CPD-17523]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20918`

## Notes

CPD-17523 + KDO2-LIPID-A -> 2-Acylglycero-Phosphocholines + CPD-22536; direction=PHYSIOL-LEFT-TO-RIGHT
