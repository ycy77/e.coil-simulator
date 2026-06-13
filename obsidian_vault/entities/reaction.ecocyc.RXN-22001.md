---
entity_id: "reaction.ecocyc.RXN-22001"
entity_type: "reaction"
name: "RXN-22001"
source_database: "EcoCyc"
source_id: "RXN-22001"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22001

`reaction.ecocyc.RXN-22001`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22001`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + Reduced-Flavorubredoxins + PROTON -> NADH + Oxidized-Flavorubredoxins; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: NAD + Reduced-Flavorubredoxins + PROTON -> NADH + Oxidized-Flavorubredoxins; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by norW (protein.P37596). Substrates: NAD+ (molecule.C00003), H+ (molecule.C00080). Products: NADH (molecule.C00004).

## Annotation

NAD + Reduced-Flavorubredoxins + PROTON -> NADH + Oxidized-Flavorubredoxins; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P37596|protein.P37596]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22001`

## Notes

NAD + Reduced-Flavorubredoxins + PROTON -> NADH + Oxidized-Flavorubredoxins; direction=PHYSIOL-RIGHT-TO-LEFT
