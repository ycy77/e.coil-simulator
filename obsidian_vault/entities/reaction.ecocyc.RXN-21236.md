---
entity_id: "reaction.ecocyc.RXN-21236"
entity_type: "reaction"
name: "RXN-21236"
source_database: "EcoCyc"
source_id: "RXN-21236"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21236

`reaction.ecocyc.RXN-21236`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21236`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A-2-METHYLTHIOCYTOSINE32-IN-TRNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 2-Thiocytosine-32-In-tRNAs + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: A-2-METHYLTHIOCYTOSINE32-IN-TRNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 2-Thiocytosine-32-In-tRNAs + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), a 2-methylthiocytosine32 in tRNA (molecule.ecocyc.A-2-METHYLTHIOCYTOSINE32-IN-TRNA). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Formaldehyde (molecule.C00067), a 2-thiocytosine32 in tRNA (molecule.ecocyc.2-Thiocytosine-32-In-tRNAs).

## Annotation

A-2-METHYLTHIOCYTOSINE32-IN-TRNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 2-Thiocytosine-32-In-tRNAs + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-Thiocytosine-32-In-tRNAs|molecule.ecocyc.2-Thiocytosine-32-In-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.A-2-METHYLTHIOCYTOSINE32-IN-TRNA|molecule.ecocyc.A-2-METHYLTHIOCYTOSINE32-IN-TRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21236`

## Notes

A-2-METHYLTHIOCYTOSINE32-IN-TRNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 2-Thiocytosine-32-In-tRNAs + FORMALDEHYDE + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
