---
entity_id: "reaction.ecocyc.RXN0-2022"
entity_type: "reaction"
name: "RXN0-2022"
source_database: "EcoCyc"
source_id: "RXN0-2022"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2022

`reaction.ecocyc.RXN0-2022`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2022`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + PYRUVATE + ACETALD -> ACETOIN + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + PYRUVATE + ACETALD -> ACETOIN + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyruvate oxidase (complex.ecocyc.PYRUVOXID-CPLX). Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080), Acetaldehyde (molecule.C00084). Products: CO2 (molecule.C00011), acetoin (molecule.ecocyc.ACETOIN).

## Annotation

PROTON + PYRUVATE + ACETALD -> ACETOIN + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.PYRUVOXID-CPLX|complex.ecocyc.PYRUVOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ACETOIN|molecule.ecocyc.ACETOIN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2022`

## Notes

PROTON + PYRUVATE + ACETALD -> ACETOIN + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
