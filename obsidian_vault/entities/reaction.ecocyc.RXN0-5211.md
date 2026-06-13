---
entity_id: "reaction.ecocyc.RXN0-5211"
entity_type: "reaction"
name: "RXN0-5211"
source_database: "EcoCyc"
source_id: "RXN0-5211"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5211

`reaction.ecocyc.RXN0-5211`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5211`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

EG10443-MONOMER + ATP -> HIPA-P + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: EG10443-MONOMER + ATP -> HIPA-P + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hipA (protein.P23874). Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Annotation

EG10443-MONOMER + ATP -> HIPA-P + ADP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P23874|protein.P23874]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5211`

## Notes

EG10443-MONOMER + ATP -> HIPA-P + ADP; direction=LEFT-TO-RIGHT
