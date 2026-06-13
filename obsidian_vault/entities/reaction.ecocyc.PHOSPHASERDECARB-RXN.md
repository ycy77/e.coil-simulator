---
entity_id: "reaction.ecocyc.PHOSPHASERDECARB-RXN"
entity_type: "reaction"
name: "PHOSPHASERDECARB-RXN"
source_database: "EcoCyc"
source_id: "PHOSPHASERDECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSPHASERDECARB-RXN

`reaction.ecocyc.PHOSPHASERDECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSPHASERDECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the final reaction in the biosynthesis of phosphatidylethanolamine. EcoCyc reaction equation: L-1-PHOSPHATIDYL-SERINE + PROTON -> L-1-PHOSPHATIDYL-ETHANOLAMINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT. This is the final reaction in the biosynthesis of phosphatidylethanolamine.

## Biological Role

Catalyzed by phosphatidylserine decarboxylase (complex.ecocyc.PHOSPHASERDECARB-DIMER). Substrates: H+ (molecule.C00080), Phosphatidylserine (molecule.C02737). Products: CO2 (molecule.C00011), Phosphatidylethanolamine (molecule.C00350).

## Enriched Pathways

- `ecocyc.PWY-5669` phosphatidylserine and phosphatidylethanolamine biosynthesis I (EcoCyc)

## Annotation

This is the final reaction in the biosynthesis of phosphatidylethanolamine.

## Pathways

- `ecocyc.PWY-5669` phosphatidylserine and phosphatidylethanolamine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.PHOSPHASERDECARB-DIMER|complex.ecocyc.PHOSPHASERDECARB-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02737|molecule.C02737]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05361|molecule.C05361]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BOROHYDRIDE|molecule.ecocyc.BOROHYDRIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1399|molecule.ecocyc.CPD0-1399]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PHOSPHASERDECARB-RXN`

## Notes

L-1-PHOSPHATIDYL-SERINE + PROTON -> L-1-PHOSPHATIDYL-ETHANOLAMINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
