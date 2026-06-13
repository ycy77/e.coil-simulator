---
entity_id: "reaction.ecocyc.RXN-8506"
entity_type: "reaction"
name: "RXN-8506"
source_database: "EcoCyc"
source_id: "RXN-8506"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8506

`reaction.ecocyc.RXN-8506`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8506`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FADH2 + NAD -> FAD + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: FADH2 + NAD -> FAD + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by fre (protein.P0AEN1), ahpF (protein.P35340). Substrates: NAD+ (molecule.C00003), FADH2 (molecule.C01352). Products: NADH (molecule.C00004), FAD (molecule.C00016), H+ (molecule.C00080).

## Annotation

FADH2 + NAD -> FAD + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AEN1|protein.P0AEN1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P35340|protein.P35340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01352|molecule.C01352]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8506`

## Notes

FADH2 + NAD -> FAD + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
