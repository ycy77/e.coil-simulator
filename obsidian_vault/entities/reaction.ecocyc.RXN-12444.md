---
entity_id: "reaction.ecocyc.RXN-12444"
entity_type: "reaction"
name: "RXN-12444"
source_database: "EcoCyc"
source_id: "RXN-12444"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12444

`reaction.ecocyc.RXN-12444`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12444`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FMNH2 + NADP -> FMN + NADPH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: FMNH2 + NADP -> FMN + NADPH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by NADPH-dependent FMN reductase (complex.ecocyc.CPLX0-224). Substrates: NADP+ (molecule.C00006), Reduced FMN (molecule.C01847). Products: NADPH (molecule.C00005), FMN (molecule.C00061), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.ALKANEMONOX-PWY` two-component alkanesulfonate monooxygenase (EcoCyc)

## Annotation

FMNH2 + NADP -> FMN + NADPH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.ALKANEMONOX-PWY` two-component alkanesulfonate monooxygenase (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-224|complex.ecocyc.CPLX0-224]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12444`

## Notes

FMNH2 + NADP -> FMN + NADPH + PROTON; direction=RIGHT-TO-LEFT
