---
entity_id: "reaction.ecocyc.RXN0-7501"
entity_type: "reaction"
name: "phosphatidylhomoserine decaroxylase"
source_database: "EcoCyc"
source_id: "RXN0-7501"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# phosphatidylhomoserine decaroxylase

`reaction.ecocyc.RXN0-7501`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7501`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2733 + PROTON -> CPD0-2734 + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2733 + PROTON -> CPD0-2734 + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a phosphatidylhomoserine (molecule.ecocyc.CPD0-2733). Products: CO2 (molecule.C00011), a phosphatidylpropanolamine (molecule.ecocyc.CPD0-2734).

## Enriched Pathways

- `ecocyc.PWY0-1644` phosphatidylhomoserine and phosphatidylpropanolamine biosynthesis (EcoCyc)

## Annotation

CPD0-2733 + PROTON -> CPD0-2734 + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1644` phosphatidylhomoserine and phosphatidylpropanolamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2734|molecule.ecocyc.CPD0-2734]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2733|molecule.ecocyc.CPD0-2733]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7501`

## Notes

CPD0-2733 + PROTON -> CPD0-2734 + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
