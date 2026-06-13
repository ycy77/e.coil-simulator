---
entity_id: "reaction.ecocyc.RXN0-6727"
entity_type: "reaction"
name: "RXN0-6727"
source_database: "EcoCyc"
source_id: "RXN0-6727"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6727

`reaction.ecocyc.RXN0-6727`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6727`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-653 + ADP -> PROTON + NADH + AMP + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-653 + ADP -> PROTON + NADH + AMP + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nnr (protein.P31806). Substrates: ADP (molecule.C00008), (S)-NADHX (molecule.ecocyc.CPD-653). Products: NADH (molecule.C00004), AMP (molecule.C00020), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-653 + ADP -> PROTON + NADH + AMP + Pi; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P31806|protein.P31806]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-653|molecule.ecocyc.CPD-653]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6727`

## Notes

CPD-653 + ADP -> PROTON + NADH + AMP + Pi; direction=LEFT-TO-RIGHT
