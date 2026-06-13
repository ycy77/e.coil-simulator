---
entity_id: "reaction.ecocyc.THIKIN-RXN"
entity_type: "reaction"
name: "THIKIN-RXN"
source_database: "EcoCyc"
source_id: "THIKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THIKIN-RXN

`reaction.ecocyc.THIKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THIKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first reaction in the conversion of thiamin to thiamin pyrophosphate. It is another route to thiamin-P. EcoCyc reaction equation: THIAMINE + ATP -> PROTON + THIAMINE-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. The first reaction in the conversion of thiamin to thiamin pyrophosphate. It is another route to thiamin-P.

## Biological Role

Catalyzed by thiK (protein.P75948). Substrates: ATP (molecule.C00002), Thiamine (molecule.C00378). Products: ADP (molecule.C00008), H+ (molecule.C00080), Thiamin monophosphate (molecule.C01081).

## Annotation

The first reaction in the conversion of thiamin to thiamin pyrophosphate. It is another route to thiamin-P.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P75948|protein.P75948]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01081|molecule.C01081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00378|molecule.C00378]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THIKIN-RXN`

## Notes

THIAMINE + ATP -> PROTON + THIAMINE-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
