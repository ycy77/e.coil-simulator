---
entity_id: "reaction.ecocyc.RXN-18739"
entity_type: "reaction"
name: "RXN-18739"
source_database: "EcoCyc"
source_id: "RXN-18739"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18739

`reaction.ecocyc.RXN-18739`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18739`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-20035 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DAMP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20035 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DAMP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), 1-methyl-dAMP (molecule.ecocyc.CPD-20035). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Formaldehyde (molecule.C00067), dAMP (molecule.C00360).

## Annotation

CPD-20035 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DAMP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00360|molecule.C00360]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20035|molecule.ecocyc.CPD-20035]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18739`

## Notes

CPD-20035 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DAMP + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
