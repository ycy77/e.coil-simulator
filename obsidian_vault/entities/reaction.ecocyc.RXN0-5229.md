---
entity_id: "reaction.ecocyc.RXN0-5229"
entity_type: "reaction"
name: "RXN0-5229"
source_database: "EcoCyc"
source_id: "RXN0-5229"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5229

`reaction.ecocyc.RXN0-5229`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5229`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1083 + NAD -> PROTON + D-TAGATURONATE + NADH; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1083 + NAD -> PROTON + D-TAGATURONATE + NADH; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lgoD (protein.P39400). Substrates: NAD+ (molecule.C00003), L-Galactonate (molecule.C15930). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Tagaturonate (molecule.C00558).

## Enriched Pathways

- `ecocyc.PWY0-1306` L-galactonate degradation (EcoCyc)

## Annotation

CPD0-1083 + NAD -> PROTON + D-TAGATURONATE + NADH; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1306` L-galactonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39400|protein.P39400]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00558|molecule.C00558]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15930|molecule.C15930]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5229`

## Notes

CPD0-1083 + NAD -> PROTON + D-TAGATURONATE + NADH; direction=LEFT-TO-RIGHT
