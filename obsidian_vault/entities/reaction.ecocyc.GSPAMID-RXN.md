---
entity_id: "reaction.ecocyc.GSPAMID-RXN"
entity_type: "reaction"
name: "GSPAMID-RXN"
source_database: "EcoCyc"
source_id: "GSPAMID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GSPAMID-RXN

`reaction.ecocyc.GSPAMID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GSPAMID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction hydrolyzes the amide bond of glutathionylspermidine. EcoCyc reaction equation: GLUTATHIONYLSPERMIDINE + WATER -> GLUTATHIONE + SPERMIDINE; direction=LEFT-TO-RIGHT. This reaction hydrolyzes the amide bond of glutathionylspermidine.

## Biological Role

Catalyzed by fused glutathionylspermidine amidase / glutathionylspermidine synthetase (complex.ecocyc.GSP-CPLX). Substrates: H2O (molecule.C00001), Glutathionylspermidine (molecule.C05730). Products: Glutathione (molecule.C00051), Spermidine (molecule.C00315).

## Annotation

This reaction hydrolyzes the amide bond of glutathionylspermidine.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.GSP-CPLX|complex.ecocyc.GSP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05730|molecule.C05730]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1891|molecule.ecocyc.CPD0-1891]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GSPAMID-RXN`

## Notes

GLUTATHIONYLSPERMIDINE + WATER -> GLUTATHIONE + SPERMIDINE; direction=LEFT-TO-RIGHT
