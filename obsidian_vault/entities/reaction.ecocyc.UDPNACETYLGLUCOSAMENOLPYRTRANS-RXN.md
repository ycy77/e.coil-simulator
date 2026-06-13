---
entity_id: "reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN"
entity_type: "reaction"
name: "UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN"
source_database: "EcoCyc"
source_id: "UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN

`reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first committed step in peptidoglycan biosynthesis. EcoCyc reaction equation: UDP-N-ACETYL-D-GLUCOSAMINE + PHOSPHO-ENOL-PYRUVATE -> UDP-ACETYL-CARBOXYVINYL-GLUCOSAMINE + Pi; direction=LEFT-TO-RIGHT. This is the first committed step in peptidoglycan biosynthesis.

## Biological Role

Catalyzed by murA (protein.P0A749). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043), Phosphoenolpyruvate (molecule.C00074). Products: UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine (molecule.C04631), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)
- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

This is the first committed step in peptidoglycan biosynthesis.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)
- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A749|protein.P0A749]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04631|molecule.C04631]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BROMOACETATE|molecule.ecocyc.BROMOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-14021|molecule.ecocyc.CPD-14021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1113|molecule.ecocyc.CPD0-1113]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN`

## Notes

UDP-N-ACETYL-D-GLUCOSAMINE + PHOSPHO-ENOL-PYRUVATE -> UDP-ACETYL-CARBOXYVINYL-GLUCOSAMINE + Pi; direction=LEFT-TO-RIGHT
