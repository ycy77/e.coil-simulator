---
entity_id: "reaction.ecocyc.RXN0-5210"
entity_type: "reaction"
name: "RXN0-5210"
source_database: "EcoCyc"
source_id: "RXN0-5210"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5210

`reaction.ecocyc.RXN0-5210`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5210`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1048 + UDP-D-GALACTO-14-FURANOSE -> PROTON + CPD0-1049 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1048 + UDP-D-GALACTO-14-FURANOSE -> PROTON + CPD0-1049 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wbbI (protein.P37749). Substrates: UDP-alpha-D-galactofuranose (molecule.C03733), octyl α-D-glucopyranoside (molecule.ecocyc.CPD0-1048). Products: UDP (molecule.C00015), H+ (molecule.C00080), octyl β-1,6-D-galactofuranosyl-α-D-glucopyranoside (molecule.ecocyc.CPD0-1049).

## Annotation

CPD0-1048 + UDP-D-GALACTO-14-FURANOSE -> PROTON + CPD0-1049 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37749|protein.P37749]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1049|molecule.ecocyc.CPD0-1049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03733|molecule.C03733]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1048|molecule.ecocyc.CPD0-1048]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5210`

## Notes

CPD0-1048 + UDP-D-GALACTO-14-FURANOSE -> PROTON + CPD0-1049 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
