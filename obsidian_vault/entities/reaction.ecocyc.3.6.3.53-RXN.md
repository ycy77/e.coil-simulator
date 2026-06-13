---
entity_id: "reaction.ecocyc.3.6.3.53-RXN"
entity_type: "reaction"
name: "3.6.3.53-RXN"
source_database: "EcoCyc"
source_id: "3.6.3.53-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.6.3.53-RXN

`reaction.ecocyc.3.6.3.53-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.6.3.53-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

AG+ + ATP + WATER -> AG+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: AG+ + ATP + WATER -> AG+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Ag+ (molecule.ecocyc.AG_). Products: ADP (molecule.C00008), H+ (molecule.C00080), Ag+ (molecule.ecocyc.AG_), phosphate (molecule.ecocyc.Pi).

## Annotation

AG+ + ATP + WATER -> AG+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.6.3.53-RXN`

## Notes

AG+ + ATP + WATER -> AG+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
