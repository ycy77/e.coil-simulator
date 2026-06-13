---
entity_id: "reaction.ecocyc.RXN0-7280"
entity_type: "reaction"
name: "RXN0-7280"
source_database: "EcoCyc"
source_id: "RXN0-7280"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7280

`reaction.ecocyc.RXN0-7280`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7280`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-20036 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DATP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20036 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DATP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), 1-methyl-dATP (molecule.ecocyc.CPD-20036). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Formaldehyde (molecule.C00067), dATP (molecule.C00131).

## Annotation

CPD-20036 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DATP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20036|molecule.ecocyc.CPD-20036]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7280`

## Notes

CPD-20036 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DATP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
