---
entity_id: "reaction.ecocyc.RXN-13141"
entity_type: "reaction"
name: "RXN-13141"
source_database: "EcoCyc"
source_id: "RXN-13141"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13141

`reaction.ecocyc.RXN-13141`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13141`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2474 + ADP -> NADPH + AMP + Pi + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2474 + ADP -> NADPH + AMP + Pi + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nnr (protein.P31806). Substrates: ADP (molecule.C00008), (S)-NADPHX (molecule.ecocyc.CPD0-2474). Products: NADPH (molecule.C00005), AMP (molecule.C00020), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD0-2474 + ADP -> NADPH + AMP + Pi + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P31806|protein.P31806]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2474|molecule.ecocyc.CPD0-2474]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13141`

## Notes

CPD0-2474 + ADP -> NADPH + AMP + Pi + PROTON; direction=LEFT-TO-RIGHT
