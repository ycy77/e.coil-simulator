---
entity_id: "reaction.ecocyc.RXN0-7450"
entity_type: "reaction"
name: "RXN0-7450"
source_database: "EcoCyc"
source_id: "RXN0-7450"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7450

`reaction.ecocyc.RXN0-7450`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7450`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MONOMER0-4152 + Protein-Dithiols -> DISULFOXRED-MONOMER + Protein-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MONOMER0-4152 + Protein-Dithiols -> DISULFOXRED-MONOMER + Protein-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dsbA (protein.P0AEG4). Substrates: a [protein]-dithiol (molecule.ecocyc.Protein-Dithiols). Products: a [protein]-disulfide (molecule.ecocyc.Protein-Disulfides).

## Annotation

MONOMER0-4152 + Protein-Dithiols -> DISULFOXRED-MONOMER + Protein-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AEG4|protein.P0AEG4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Protein-Disulfides|molecule.ecocyc.Protein-Disulfides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Dithiols|molecule.ecocyc.Protein-Dithiols]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7450`

## Notes

MONOMER0-4152 + Protein-Dithiols -> DISULFOXRED-MONOMER + Protein-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT
