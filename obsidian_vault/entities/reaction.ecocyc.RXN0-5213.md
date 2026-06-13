---
entity_id: "reaction.ecocyc.RXN0-5213"
entity_type: "reaction"
name: "RXN0-5213"
source_database: "EcoCyc"
source_id: "RXN0-5213"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5213

`reaction.ecocyc.RXN0-5213`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5213`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + METHYL-GLYOXAL + NADH -> ACETOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + METHYL-GLYOXAL + NADH -> ACETOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ydjG (protein.P77256). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), Methylglyoxal (molecule.C00546). Products: NAD+ (molecule.C00003), Hydroxyacetone (molecule.C05235).

## Annotation

PROTON + METHYL-GLYOXAL + NADH -> ACETOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77256|protein.P77256]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05235|molecule.C05235]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5213`

## Notes

PROTON + METHYL-GLYOXAL + NADH -> ACETOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
