---
entity_id: "reaction.ecocyc.ASPDECARBOX-RXN"
entity_type: "reaction"
name: "ASPDECARBOX-RXN"
source_database: "EcoCyc"
source_id: "ASPDECARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASPDECARBOX-RXN

`reaction.ecocyc.ASPDECARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPDECARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is responsible for the biosynthesis of β-alanine, needed for pantothenate biosynthesis. EcoCyc reaction equation: PROTON + L-ASPARTATE -> B-ALANINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT. This reaction is responsible for the biosynthesis of β-alanine, needed for pantothenate biosynthesis.

## Biological Role

Catalyzed by aspartate 1-decarboxylase (complex.ecocyc.CPLX0-2901). Substrates: L-Aspartate (molecule.C00049), H+ (molecule.C00080). Products: CO2 (molecule.C00011), beta-Alanine (molecule.C00099).

## Enriched Pathways

- `ecocyc.PWY-5155` β-alanine biosynthesis III (EcoCyc)

## Annotation

This reaction is responsible for the biosynthesis of β-alanine, needed for pantothenate biosynthesis.

## Pathways

- `ecocyc.PWY-5155` β-alanine biosynthesis III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2901|complex.ecocyc.CPLX0-2901]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00099|molecule.C00099]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05361|molecule.C05361]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BH4NA|molecule.ecocyc.BH4NA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2482|molecule.ecocyc.CPD-2482]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P37613|protein.P37613]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPDECARBOX-RXN`

## Notes

PROTON + L-ASPARTATE -> B-ALANINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
