---
entity_id: "reaction.ecocyc.ENTF-RXN"
entity_type: "reaction"
name: "ENTF-RXN"
source_database: "EcoCyc"
source_id: "ENTF-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENTF-RXN

`reaction.ecocyc.ENTF-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENTF-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction L-serine is activated for incorporation into enterobactin. The reaction is ATP-dependent and the product L-seryl-AMP remains enzyme bound. EcoCyc reaction equation: SER + ATP + PROTON -> PPI + SERYL-AMP; direction=PHYSIOL-LEFT-TO-RIGHT. In this reaction L-serine is activated for incorporation into enterobactin. The reaction is ATP-dependent and the product L-seryl-AMP remains enzyme bound.

## Biological Role

Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-seryl)adenylate (molecule.ecocyc.SERYL-AMP).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

In this reaction L-serine is activated for incorporation into enterobactin. The reaction is ATP-dependent and the product L-seryl-AMP remains enzyme bound.

## Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SERYL-AMP|molecule.ecocyc.SERYL-AMP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ENTF-RXN`

## Notes

SER + ATP + PROTON -> PPI + SERYL-AMP; direction=PHYSIOL-LEFT-TO-RIGHT
