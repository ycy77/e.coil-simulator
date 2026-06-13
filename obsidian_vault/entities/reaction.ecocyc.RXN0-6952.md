---
entity_id: "reaction.ecocyc.RXN0-6952"
entity_type: "reaction"
name: "RXN0-6952"
source_database: "EcoCyc"
source_id: "RXN0-6952"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6952

`reaction.ecocyc.RXN0-6952`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6952`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

HAS A MUCH BROADER SPECIFICITY THAN EC 3.1.1.4. EcoCyc reaction equation: L-1-PHOSPHATIDYL-ETHANOLAMINE + WATER -> 2-ACYL-GPE + Fatty-Acids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. HAS A MUCH BROADER SPECIFICITY THAN EC 3.1.1.4.

## Biological Role

Catalyzed by outer membrane phospholipase A (complex.ecocyc.CPLX0-7944). Substrates: H2O (molecule.C00001), Phosphatidylethanolamine (molecule.C00350). Products: H+ (molecule.C00080), Fatty acid (molecule.C00162), 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973).

## Annotation

HAS A MUCH BROADER SPECIFICITY THAN EC 3.1.1.4.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7944|complex.ecocyc.CPLX0-7944]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00162|molecule.C00162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05973|molecule.C05973]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-20862|molecule.ecocyc.CPD-20862]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6952`

## Notes

L-1-PHOSPHATIDYL-ETHANOLAMINE + WATER -> 2-ACYL-GPE + Fatty-Acids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
