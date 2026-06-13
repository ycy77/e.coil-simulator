---
entity_id: "reaction.ecocyc.RXN0-1139"
entity_type: "reaction"
name: "RXN0-1139"
source_database: "EcoCyc"
source_id: "RXN0-1139"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1139

`reaction.ecocyc.RXN0-1139`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1139`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + E2P-MONOMER + LIPOIC-ACID -> AMP + PPI + ACEF-LIPOATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + E2P-MONOMER + LIPOIC-ACID -> AMP + PPI + ACEF-LIPOATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lplA (protein.P32099). Substrates: ATP (molecule.C00002), (R)-Lipoate (molecule.C16241). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

ATP + E2P-MONOMER + LIPOIC-ACID -> AMP + PPI + ACEF-LIPOATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P32099|protein.P32099]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.6-SELENO-OCTANOATE|molecule.ecocyc.6-SELENO-OCTANOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.8-SELENO-OCTANOATE|molecule.ecocyc.8-SELENO-OCTANOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.8-THIO-OCTANOATE|molecule.ecocyc.8-THIO-OCTANOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-1139`

## Notes

ATP + E2P-MONOMER + LIPOIC-ACID -> AMP + PPI + ACEF-LIPOATE; direction=PHYSIOL-LEFT-TO-RIGHT
