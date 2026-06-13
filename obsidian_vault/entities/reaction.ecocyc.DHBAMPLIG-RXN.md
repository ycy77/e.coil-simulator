---
entity_id: "reaction.ecocyc.DHBAMPLIG-RXN"
entity_type: "reaction"
name: "DHBAMPLIG-RXN"
source_database: "EcoCyc"
source_id: "DHBAMPLIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DHBAMPLIG-RXN

`reaction.ecocyc.DHBAMPLIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DHBAMPLIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction 2,3-dihydroxybenzoate is activated. The reaction is ATP-dependent and the product (2,3-dihydroxybenzoyl)adenylate remains enzyme bound. EcoCyc reaction equation: PROTON + ATP + 2-3-DIHYDROXYBENZOATE -> PPI + CPD-62; direction=PHYSIOL-LEFT-TO-RIGHT. In this reaction 2,3-dihydroxybenzoate is activated. The reaction is ATP-dependent and the product (2,3-dihydroxybenzoyl)adenylate remains enzyme bound.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), 2,3-Dihydroxybenzoate (molecule.C00196). Products: Diphosphate (molecule.C00013), (2,3-dihydroxybenzoyl)adenylate (molecule.ecocyc.CPD-62).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

In this reaction 2,3-dihydroxybenzoate is activated. The reaction is ATP-dependent and the product (2,3-dihydroxybenzoyl)adenylate remains enzyme bound.

## Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-62|molecule.ecocyc.CPD-62]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00196|molecule.C00196]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DHBAMPLIG-RXN`

## Notes

PROTON + ATP + 2-3-DIHYDROXYBENZOATE -> PPI + CPD-62; direction=PHYSIOL-LEFT-TO-RIGHT
