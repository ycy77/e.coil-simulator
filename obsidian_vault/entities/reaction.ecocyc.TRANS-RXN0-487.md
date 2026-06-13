---
entity_id: "reaction.ecocyc.TRANS-RXN0-487"
entity_type: "reaction"
name: "Mn2+ export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-487"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Mn2+ export

`reaction.ecocyc.TRANS-RXN0-487`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-487`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MN+2 -> MN+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MN+2 -> MN+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alx (protein.P42601), mntP (protein.P76264). Substrates: Mn2+ (molecule.ecocyc.MN_2). Products: Mn2+ (molecule.ecocyc.MN_2).

## Annotation

MN+2 -> MN+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P42601|protein.P42601]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76264|protein.P76264]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-487`

## Notes

MN+2 -> MN+2; direction=LEFT-TO-RIGHT
