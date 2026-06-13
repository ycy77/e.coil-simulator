---
entity_id: "reaction.ecocyc.MMUM-RXN"
entity_type: "reaction"
name: "MMUM-RXN"
source_database: "EcoCyc"
source_id: "MMUM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MMUM-RXN

`reaction.ecocyc.MMUM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MMUM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-397 + HOMO-CYS -> PROTON + MET; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-397 + HOMO-CYS -> PROTON + MET; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mmuM (protein.Q47690). Substrates: L-Homocysteine (molecule.C00155), S-Methyl-L-methionine (molecule.C03172). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080).

## Annotation

CPD-397 + HOMO-CYS -> PROTON + MET; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q47690|protein.Q47690]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03172|molecule.C03172]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MMUM-RXN`

## Notes

CPD-397 + HOMO-CYS -> PROTON + MET; direction=PHYSIOL-LEFT-TO-RIGHT
