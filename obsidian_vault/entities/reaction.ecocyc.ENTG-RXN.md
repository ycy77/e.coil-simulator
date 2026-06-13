---
entity_id: "reaction.ecocyc.ENTG-RXN"
entity_type: "reaction"
name: "ENTG-RXN"
source_database: "EcoCyc"
source_id: "ENTG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENTG-RXN

`reaction.ecocyc.ENTG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENTG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction or reactions are involved in the final steps of the synthesis of enterobactin, cyclizing and ligating the L-seryl-AMP and the (2,3-dihydroxybenzoyl)adenylate. EcoCyc reaction equation: DHB-Seryl-EntF -> ENTEROBACTIN + Holo-EntF; direction=LEFT-TO-RIGHT. This reaction or reactions are involved in the final steps of the synthesis of enterobactin, cyclizing and ligating the L-seryl-AMP and the (2,3-dihydroxybenzoyl)adenylate.

## Biological Role

Catalyzed by entF (protein.P11454). Products: Enterochelin (molecule.C05821).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

This reaction or reactions are involved in the final steps of the synthesis of enterobactin, cyclizing and ligating the L-seryl-AMP and the (2,3-dihydroxybenzoyl)adenylate.

## Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P11454|protein.P11454]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:ENTG-RXN`

## Notes

DHB-Seryl-EntF -> ENTEROBACTIN + Holo-EntF; direction=LEFT-TO-RIGHT
