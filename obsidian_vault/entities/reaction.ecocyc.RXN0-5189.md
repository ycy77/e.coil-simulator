---
entity_id: "reaction.ecocyc.RXN0-5189"
entity_type: "reaction"
name: "RXN0-5189"
source_database: "EcoCyc"
source_id: "RXN0-5189"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5189

`reaction.ecocyc.RXN0-5189`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5189`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-3-methyladenines + WATER -> DNA-containing-abasic-Sites + 3-Methyl-Adenines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-3-methyladenines + WATER -> DNA-containing-abasic-Sites + 3-Methyl-Adenines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tag (protein.P05100). Substrates: H2O (molecule.C00001), an N3-methyladenine in DNA (molecule.ecocyc.DNA-3-methyladenines). Products: 3-methyladenine (molecule.ecocyc.3-Methyl-Adenines).

## Annotation

DNA-3-methyladenines + WATER -> DNA-containing-abasic-Sites + 3-Methyl-Adenines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P05100|protein.P05100]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.3-Methyl-Adenines|molecule.ecocyc.3-Methyl-Adenines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-3-methyladenines|molecule.ecocyc.DNA-3-methyladenines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5189`

## Notes

DNA-3-methyladenines + WATER -> DNA-containing-abasic-Sites + 3-Methyl-Adenines; direction=PHYSIOL-LEFT-TO-RIGHT
