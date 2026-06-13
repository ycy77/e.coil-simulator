---
entity_id: "reaction.ecocyc.3.2.2.21-RXN"
entity_type: "reaction"
name: "3.2.2.21-RXN"
source_database: "EcoCyc"
source_id: "3.2.2.21-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DNA glycosidase II"
---

# 3.2.2.21-RXN

`reaction.ecocyc.3.2.2.21-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.2.2.21-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Alkylated-DNAs + WATER -> DNA-containing-abasic-Sites + Alkylated-Bases; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Alkylated-DNAs + WATER -> DNA-containing-abasic-Sites + Alkylated-Bases; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkA (protein.P04395). Substrates: H2O (molecule.C00001). Products: an alkylated nucleobase (molecule.ecocyc.Alkylated-Bases).

## Annotation

Alkylated-DNAs + WATER -> DNA-containing-abasic-Sites + Alkylated-Bases; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P04395|protein.P04395]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Alkylated-Bases|molecule.ecocyc.Alkylated-Bases]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.2.2.21-RXN`

## Notes

Alkylated-DNAs + WATER -> DNA-containing-abasic-Sites + Alkylated-Bases; direction=PHYSIOL-LEFT-TO-RIGHT
