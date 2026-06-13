---
entity_id: "reaction.ecocyc.RXN0-6554"
entity_type: "reaction"
name: "RXN0-6554"
source_database: "EcoCyc"
source_id: "RXN0-6554"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6554

`reaction.ecocyc.RXN0-6554`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6554`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

DI-H-OROTATE + Menaquinones -> OROTATE + Menaquinols; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DI-H-OROTATE + Menaquinones -> OROTATE + Menaquinols; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyrD (protein.P0A7E1). Substrates: (S)-Dihydroorotate (molecule.C00337), Menaquinone (molecule.C00828). Products: Orotate (molecule.C00295), Menaquinol (molecule.C05819).

## Annotation

DI-H-OROTATE + Menaquinones -> OROTATE + Menaquinols; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7E1|protein.P0A7E1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00337|molecule.C00337]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6554`

## Notes

DI-H-OROTATE + Menaquinones -> OROTATE + Menaquinols; direction=LEFT-TO-RIGHT
