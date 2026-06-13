---
entity_id: "reaction.ecocyc.DIAMACTRANS-RXN"
entity_type: "reaction"
name: "DIAMACTRANS-RXN"
source_database: "EcoCyc"
source_id: "DIAMACTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIAMACTRANS-RXN

`reaction.ecocyc.DIAMACTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIAMACTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this general reaction diamines undergo acetylation. EcoCyc reaction equation: Aliphatic-Alpha-Omega-Diamines + ACETYL-COA -> Aliphatic-N-Acetyl-Diamines + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. In this general reaction diamines undergo acetylation.

## Biological Role

Catalyzed by spermidine N-acetyltransferase (complex.ecocyc.SPERMACTRAN-CPLX). Substrates: Acetyl-CoA (molecule.C00024), an aliphatic α,ω-diamine (molecule.ecocyc.Aliphatic-Alpha-Omega-Diamines). Products: CoA (molecule.C00010), H+ (molecule.C00080), Aliphatic-N-Acetyl-Diamines (molecule.ecocyc.Aliphatic-N-Acetyl-Diamines).

## Annotation

In this general reaction diamines undergo acetylation.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.SPERMACTRAN-CPLX|complex.ecocyc.SPERMACTRAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Aliphatic-N-Acetyl-Diamines|molecule.ecocyc.Aliphatic-N-Acetyl-Diamines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aliphatic-Alpha-Omega-Diamines|molecule.ecocyc.Aliphatic-Alpha-Omega-Diamines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIAMACTRANS-RXN`

## Notes

Aliphatic-Alpha-Omega-Diamines + ACETYL-COA -> Aliphatic-N-Acetyl-Diamines + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
