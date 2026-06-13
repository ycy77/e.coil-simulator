---
entity_id: "reaction.ecocyc.1.7.2.2-RXN"
entity_type: "reaction"
name: "1.7.2.2-RXN"
source_database: "EcoCyc"
source_id: "1.7.2.2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.7.2.2-RXN

`reaction.ecocyc.1.7.2.2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.7.2.2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + Cytochromes-C-Reduced + NITRITE -> WATER + AMMONIUM + Cytochromes-C-Oxidized; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + Cytochromes-C-Reduced + NITRITE -> WATER + AMMONIUM + Cytochromes-C-Oxidized; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Nitrite (molecule.C00088). Products: H2O (molecule.C00001), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

PROTON + Cytochromes-C-Reduced + NITRITE -> WATER + AMMONIUM + Cytochromes-C-Oxidized; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.7.2.2-RXN`

## Notes

PROTON + Cytochromes-C-Reduced + NITRITE -> WATER + AMMONIUM + Cytochromes-C-Oxidized; direction=LEFT-TO-RIGHT
