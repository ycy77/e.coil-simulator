---
entity_id: "reaction.ecocyc.CITTRANS-RXN"
entity_type: "reaction"
name: "CITTRANS-RXN"
source_database: "EcoCyc"
source_id: "CITTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "acetyl-CoA:citrate CoA-transferase"
  - "acetyl-ACP:citrate ACP transferase"
  - "citrate-ACP transferase"
---

# CITTRANS-RXN

`reaction.ecocyc.CITTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CITTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the two-step sequence of citrate lyase. The citryl-ACP intermediate is formed by transfer of ACP from acetyl-ACP. EcoCyc reaction equation: CIT + CITRATE-LYASE + PROTON -> Citrate-Lyase-Citryl-Form + ACET; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in the two-step sequence of citrate lyase. The citryl-ACP intermediate is formed by transfer of ACP from acetyl-ACP.

## Biological Role

Catalyzed by citrate lyase (complex.ecocyc.ACECITLY-CPLX). Substrates: H+ (molecule.C00080), Citrate (molecule.C00158). Products: Acetate (molecule.C00033).

## Enriched Pathways

- `ecocyc.PWY-6038` citrate degradation (EcoCyc)

## Annotation

This is the first reaction in the two-step sequence of citrate lyase. The citryl-ACP intermediate is formed by transfer of ACP from acetyl-ACP.

## Pathways

- `ecocyc.PWY-6038` citrate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.ACECITLY-CPLX|complex.ecocyc.ACECITLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CITTRANS-RXN`

## Notes

CIT + CITRATE-LYASE + PROTON -> Citrate-Lyase-Citryl-Form + ACET; direction=PHYSIOL-LEFT-TO-RIGHT
