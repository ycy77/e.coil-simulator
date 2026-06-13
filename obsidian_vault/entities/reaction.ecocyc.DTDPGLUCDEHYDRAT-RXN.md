---
entity_id: "reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN"
entity_type: "reaction"
name: "DTDPGLUCDEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "DTDPGLUCDEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DTDPGLUCDEHYDRAT-RXN

`reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DTDPGLUCDEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide. EcoCyc reaction equation: DTDP-D-GLUCOSE -> WATER + DTDP-DEOH-DEOXY-GLUCOSE; direction=LEFT-TO-RIGHT. This is the second step in dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide.

## Biological Role

Catalyzed by dTDP-glucose 4,6-dehydratase 1 (complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX), rffG (protein.P27830). Substrates: dTDP-glucose (molecule.C00842). Products: H2O (molecule.C00001), dTDP-4-oxo-6-deoxy-D-glucose (molecule.C11907).

## Enriched Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)
- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Annotation

This is the second step in dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide.

## Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)
- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX|complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27830|protein.P27830]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11907|molecule.C11907]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00842|molecule.C00842]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2617|molecule.ecocyc.CPD0-2617]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Sulfhydryls|molecule.ecocyc.Sulfhydryls]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DTDPGLUCDEHYDRAT-RXN`

## Notes

DTDP-D-GLUCOSE -> WATER + DTDP-DEOH-DEOXY-GLUCOSE; direction=LEFT-TO-RIGHT
