---
entity_id: "reaction.ecocyc.HISTPRATPHYD-RXN"
entity_type: "reaction"
name: "HISTPRATPHYD-RXN"
source_database: "EcoCyc"
source_id: "HISTPRATPHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HISTPRATPHYD-RXN

`reaction.ecocyc.HISTPRATPHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HISTPRATPHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in the biosynthesis of histidine EcoCyc reaction equation: PHOSPHORIBOSYL-ATP + WATER -> PHOSPHORIBOSYL-AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in the biosynthesis of histidine

## Biological Role

Catalyzed by hisI (protein.P06989). Substrates: H2O (molecule.C00001), 1-(5-Phospho-D-ribosyl)-ATP (molecule.C02739). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), Phosphoribosyl-AMP (molecule.C02741).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This is the second step in the biosynthesis of histidine

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06989|protein.P06989]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02741|molecule.C02741]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02739|molecule.C02739]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HISTPRATPHYD-RXN`

## Notes

PHOSPHORIBOSYL-ATP + WATER -> PHOSPHORIBOSYL-AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
