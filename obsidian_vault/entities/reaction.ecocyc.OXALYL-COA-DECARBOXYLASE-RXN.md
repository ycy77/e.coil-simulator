---
entity_id: "reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN"
entity_type: "reaction"
name: "OXALYL-COA-DECARBOXYLASE-RXN"
source_database: "EcoCyc"
source_id: "OXALYL-COA-DECARBOXYLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OXALYL-COA-DECARBOXYLASE-RXN

`reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OXALYL-COA-DECARBOXYLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + OXALYL-COA -> CARBON-DIOXIDE + FORMYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + OXALYL-COA -> CARBON-DIOXIDE + FORMYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by oxalyl-CoA decarboxylase (complex.ecocyc.CPLX0-7878). Substrates: H+ (molecule.C00080), Oxalyl-CoA (molecule.C00313). Products: CO2 (molecule.C00011), Formyl-CoA (molecule.C00798).

## Annotation

PROTON + OXALYL-COA -> CARBON-DIOXIDE + FORMYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7878|complex.ecocyc.CPLX0-7878]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00798|molecule.C00798]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00313|molecule.C00313]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:OXALYL-COA-DECARBOXYLASE-RXN`

## Notes

PROTON + OXALYL-COA -> CARBON-DIOXIDE + FORMYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT
