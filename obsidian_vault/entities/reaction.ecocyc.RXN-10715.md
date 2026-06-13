---
entity_id: "reaction.ecocyc.RXN-10715"
entity_type: "reaction"
name: "RXN-10715"
source_database: "EcoCyc"
source_id: "RXN-10715"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10715

`reaction.ecocyc.RXN-10715`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10715`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

INDOLE_ACETALDEHYDE + NAD + WATER -> INDOLE_ACETATE_AUXIN + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: INDOLE_ACETALDEHYDE + NAD + WATER -> INDOLE_ACETATE_AUXIN + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by puuC (protein.P23883). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Indole-3-acetaldehyde (molecule.C00637). Products: NADH (molecule.C00004), H+ (molecule.C00080), Indole-3-acetate (molecule.C00954).

## Annotation

INDOLE_ACETALDEHYDE + NAD + WATER -> INDOLE_ACETATE_AUXIN + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P23883|protein.P23883]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00954|molecule.C00954]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00637|molecule.C00637]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10715`

## Notes

INDOLE_ACETALDEHYDE + NAD + WATER -> INDOLE_ACETATE_AUXIN + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
