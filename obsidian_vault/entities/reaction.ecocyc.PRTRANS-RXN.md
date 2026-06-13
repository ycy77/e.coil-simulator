---
entity_id: "reaction.ecocyc.PRTRANS-RXN"
entity_type: "reaction"
name: "PRTRANS-RXN"
source_database: "EcoCyc"
source_id: "PRTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PR transferase"
---

# PRTRANS-RXN

`reaction.ecocyc.PRTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PRTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in the tryptophan synthesis pathway EcoCyc reaction equation: N-5-PHOSPHORIBOSYL-ANTHRANILATE + PPI -> ANTHRANILATE + PRPP; direction=RIGHT-TO-LEFT. This is the second step in the tryptophan synthesis pathway

## Biological Role

Catalyzed by trpGD (protein.P00904). Substrates: Diphosphate (molecule.C00013), N-(5-Phospho-D-ribosyl)anthranilate (molecule.C04302). Products: Anthranilate (molecule.C00108), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119).

## Enriched Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Annotation

This is the second step in the tryptophan synthesis pathway

## Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P00904|protein.P00904]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00108|molecule.C00108]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04302|molecule.C04302]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PRTRANS-RXN`

## Notes

N-5-PHOSPHORIBOSYL-ANTHRANILATE + PPI -> ANTHRANILATE + PRPP; direction=RIGHT-TO-LEFT
