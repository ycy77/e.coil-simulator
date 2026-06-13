---
entity_id: "reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN"
entity_type: "reaction"
name: "CDPDIGLYPYPHOSPHA-RXN"
source_database: "EcoCyc"
source_id: "CDPDIGLYPYPHOSPHA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CDPDIGLYPYPHOSPHA-RXN

`reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CDPDIGLYPYPHOSPHA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CDPDIACYLGLYCEROL + WATER -> L-PHOSPHATIDATE + CMP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CDPDIACYLGLYCEROL + WATER -> L-PHOSPHATIDATE + CMP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cdh (protein.P06282). Substrates: H2O (molecule.C00001), CDP-diacylglycerol (molecule.C00269). Products: CMP (molecule.C00055), H+ (molecule.C00080), Phosphatidate (molecule.C00416).

## Annotation

CDPDIACYLGLYCEROL + WATER -> L-PHOSPHATIDATE + CMP + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06282|protein.P06282]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00416|molecule.C00416]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00269|molecule.C00269]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CDPDIGLYPYPHOSPHA-RXN`

## Notes

CDPDIACYLGLYCEROL + WATER -> L-PHOSPHATIDATE + CMP + PROTON; direction=LEFT-TO-RIGHT
