---
entity_id: "reaction.ecocyc.CHEYDEPHOS-RXN"
entity_type: "reaction"
name: "CHEYDEPHOS-RXN"
source_database: "EcoCyc"
source_id: "CHEYDEPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHEYDEPHOS-RXN

`reaction.ecocyc.CHEYDEPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHEYDEPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + PHOSPHO-CHEY -> Pi + CHEY-MONOMER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + PHOSPHO-CHEY -> Pi + CHEY-MONOMER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by chemotaxis protein CheZ (complex.ecocyc.CHEZ-CPLX). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + PHOSPHO-CHEY -> Pi + CHEY-MONOMER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CHEZ-CPLX|complex.ecocyc.CHEZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions

## External IDs

- `EcoCyc:CHEYDEPHOS-RXN`

## Notes

WATER + PHOSPHO-CHEY -> Pi + CHEY-MONOMER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
