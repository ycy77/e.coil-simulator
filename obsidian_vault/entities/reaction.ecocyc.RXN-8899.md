---
entity_id: "reaction.ecocyc.RXN-8899"
entity_type: "reaction"
name: "RXN-8899"
source_database: "EcoCyc"
source_id: "RXN-8899"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8899

`reaction.ecocyc.RXN-8899`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8899`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-AMINOACRYLATE + WATER -> PYRUVATE + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 2-AMINOACRYLATE + WATER -> PYRUVATE + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), Dehydroalanine (molecule.C02218). Products: Pyruvate (molecule.C00022), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

2-AMINOACRYLATE + WATER -> PYRUVATE + AMMONIUM; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02218|molecule.C02218]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8899`

## Notes

2-AMINOACRYLATE + WATER -> PYRUVATE + AMMONIUM; direction=LEFT-TO-RIGHT
