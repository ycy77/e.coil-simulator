---
entity_id: "reaction.ecocyc.CITRYLY-RXN"
entity_type: "reaction"
name: "CITRYLY-RXN"
source_database: "EcoCyc"
source_id: "CITRYLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "(3S)-citryl-CoA oxaloacetate-lyase"
  - "citryl-ACP:oxaloacetate acetyl-ACP lyase"
  - "citryl-ACP lyase"
---

# CITRYLY-RXN

`reaction.ecocyc.CITRYLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CITRYLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the two-step sequence of citrate lyase. The citryl-ACP intermediate is cleaved with the release of oxaloacetate and the regeneration of acetyl-ACP. EcoCyc reaction equation: Citrate-Lyase-Citryl-Form -> OXALACETIC_ACID + CITRATE-LYASE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second reaction in the two-step sequence of citrate lyase. The citryl-ACP intermediate is cleaved with the release of oxaloacetate and the regeneration of acetyl-ACP.

## Biological Role

Catalyzed by citrate lyase (complex.ecocyc.ACECITLY-CPLX). Products: Oxaloacetate (molecule.C00036), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6038` citrate degradation (EcoCyc)

## Annotation

This is the second reaction in the two-step sequence of citrate lyase. The citryl-ACP intermediate is cleaved with the release of oxaloacetate and the regeneration of acetyl-ACP.

## Pathways

- `ecocyc.PWY-6038` citrate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.ACECITLY-CPLX|complex.ecocyc.ACECITLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:CITRYLY-RXN`

## Notes

Citrate-Lyase-Citryl-Form -> OXALACETIC_ACID + CITRATE-LYASE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
