---
entity_id: "reaction.ecocyc.RXN0-6732"
entity_type: "reaction"
name: "RXN0-6732"
source_database: "EcoCyc"
source_id: "RXN0-6732"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6732

`reaction.ecocyc.RXN0-6732`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6732`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1068 + ATP -> CPD0-2479 + ADENINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1068 + ATP -> CPD0-2479 + ADENINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnI (protein.P16687). Substrates: ATP (molecule.C00002), Methylphosphonate (molecule.C20396). Products: Adenine (molecule.C00147), alpha-D-Ribose 1-methylphosphonate 5-triphosphate (molecule.C20422).

## Enriched Pathways

- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Annotation

CPD0-1068 + ATP -> CPD0-2479 + ADENINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P16687|protein.P16687]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20422|molecule.C20422]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20396|molecule.C20396]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6732`

## Notes

CPD0-1068 + ATP -> CPD0-2479 + ADENINE; direction=LEFT-TO-RIGHT
