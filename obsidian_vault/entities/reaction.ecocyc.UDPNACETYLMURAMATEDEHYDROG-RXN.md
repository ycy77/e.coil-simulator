---
entity_id: "reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN"
entity_type: "reaction"
name: "UDPNACETYLMURAMATEDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "UDPNACETYLMURAMATEDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPNACETYLMURAMATEDEHYDROG-RXN

`reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPNACETYLMURAMATEDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in peptidoglycan biosynthesis. EcoCyc reaction equation: NADP + UDP-N-ACETYLMURAMATE -> PROTON + NADPH + UDP-ACETYL-CARBOXYVINYL-GLUCOSAMINE; direction=RIGHT-TO-LEFT. This is the second step in peptidoglycan biosynthesis.

## Biological Role

Catalyzed by murB (protein.P08373). Substrates: NADP+ (molecule.C00006), UDP-N-acetylmuramate (molecule.C01050). Products: NADPH (molecule.C00005), H+ (molecule.C00080), UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine (molecule.C04631).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)
- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

This is the second step in peptidoglycan biosynthesis.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)
- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P08373|protein.P08373]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04631|molecule.C04631]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UDPNACETYLMURAMATEDEHYDROG-RXN`

## Notes

NADP + UDP-N-ACETYLMURAMATE -> PROTON + NADPH + UDP-ACETYL-CARBOXYVINYL-GLUCOSAMINE; direction=RIGHT-TO-LEFT
