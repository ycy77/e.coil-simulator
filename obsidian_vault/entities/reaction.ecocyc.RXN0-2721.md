---
entity_id: "reaction.ecocyc.RXN0-2721"
entity_type: "reaction"
name: "RXN0-2721"
source_database: "EcoCyc"
source_id: "RXN0-2721"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2721

`reaction.ecocyc.RXN0-2721`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2721`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reduced-Flavorubredoxins + NITRIC-OXIDE + PROTON -> Oxidized-Flavorubredoxins + NITROUS-OXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Reduced-Flavorubredoxins + NITRIC-OXIDE + PROTON -> Oxidized-Flavorubredoxins + NITROUS-OXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by reduced flavorubredoxin (complex.ecocyc.CPLX0-1). Substrates: H+ (molecule.C00080), Nitric oxide (molecule.C00533). Products: H2O (molecule.C00001), Nitrous oxide (molecule.C00887).

## Annotation

Reduced-Flavorubredoxins + NITRIC-OXIDE + PROTON -> Oxidized-Flavorubredoxins + NITROUS-OXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1|complex.ecocyc.CPLX0-1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00887|molecule.C00887]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2721`

## Notes

Reduced-Flavorubredoxins + NITRIC-OXIDE + PROTON -> Oxidized-Flavorubredoxins + NITROUS-OXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
