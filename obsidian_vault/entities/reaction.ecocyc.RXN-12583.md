---
entity_id: "reaction.ecocyc.RXN-12583"
entity_type: "reaction"
name: "pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating)"
source_database: "EcoCyc"
source_id: "RXN-12583"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating)

`reaction.ecocyc.RXN-12583`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12583`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + PYRUVATE + THIAMINE-PYROPHOSPHATE -> 2-ALPHA-HYDROXYETHYL-THPP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + PYRUVATE + THIAMINE-PYROPHOSPHATE -> 2-ALPHA-HYDROXYETHYL-THPP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Pyruvate (molecule.C00022), Thiamin diphosphate (molecule.C00068), H+ (molecule.C00080). Products: CO2 (molecule.C00011), 2-(alpha-Hydroxyethyl)thiamine diphosphate (molecule.C05125).

## Annotation

PROTON + PYRUVATE + THIAMINE-PYROPHOSPHATE -> 2-ALPHA-HYDROXYETHYL-THPP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05125|molecule.C05125]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12583`

## Notes

PROTON + PYRUVATE + THIAMINE-PYROPHOSPHATE -> 2-ALPHA-HYDROXYETHYL-THPP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
