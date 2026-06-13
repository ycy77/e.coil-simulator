---
entity_id: "reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN"
entity_type: "reaction"
name: "PALMITOYL-COA-HYDROLASE-RXN"
source_database: "EcoCyc"
source_id: "PALMITOYL-COA-HYDROLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PALMITOYL-COA-HYDROLASE-RXN

`reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PALMITOYL-COA-HYDROLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PALMITYL-COA + WATER -> PROTON + PALMITATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PALMITYL-COA + WATER -> PROTON + PALMITATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yigI (protein.P0ADP2). Substrates: H2O (molecule.C00001), Palmitoyl-CoA (molecule.C00154). Products: CoA (molecule.C00010), H+ (molecule.C00080), Hexadecanoic acid (molecule.C00249).

## Annotation

PALMITYL-COA + WATER -> PROTON + PALMITATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ADP2|protein.P0ADP2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00249|molecule.C00249]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00154|molecule.C00154]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PALMITOYL-COA-HYDROLASE-RXN`

## Notes

PALMITYL-COA + WATER -> PROTON + PALMITATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
