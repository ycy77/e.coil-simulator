---
entity_id: "reaction.ecocyc.RXN0-3601"
entity_type: "reaction"
name: "RXN0-3601"
source_database: "EcoCyc"
source_id: "RXN0-3601"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3601

`reaction.ecocyc.RXN0-3601`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3601`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARNITINE + GAMMA-BUTYROBETAINYL-COA -> L-CARNITINYL-COA + GAMMA-BUTYROBETAINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CARNITINE + GAMMA-BUTYROBETAINYL-COA -> L-CARNITINYL-COA + GAMMA-BUTYROBETAINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by γ-butyrobetainyl-CoA:carnitine CoA transferase (complex.ecocyc.CARNDEHYDRA-CPLX). Substrates: L-carnitine (molecule.ecocyc.CARNITINE), γ-butyrobetainyl-CoA (molecule.ecocyc.GAMMA-BUTYROBETAINYL-COA). Products: 4-Trimethylammoniobutanoate (molecule.C01181), (R)-carnitinyl-CoA (molecule.ecocyc.L-CARNITINYL-COA).

## Enriched Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Annotation

CARNITINE + GAMMA-BUTYROBETAINYL-COA -> L-CARNITINYL-COA + GAMMA-BUTYROBETAINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CARNDEHYDRA-CPLX|complex.ecocyc.CARNDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01181|molecule.C01181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-CARNITINYL-COA|molecule.ecocyc.L-CARNITINYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CARNITINE|molecule.ecocyc.CARNITINE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GAMMA-BUTYROBETAINYL-COA|molecule.ecocyc.GAMMA-BUTYROBETAINYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3601`

## Notes

CARNITINE + GAMMA-BUTYROBETAINYL-COA -> L-CARNITINYL-COA + GAMMA-BUTYROBETAINE; direction=LEFT-TO-RIGHT
