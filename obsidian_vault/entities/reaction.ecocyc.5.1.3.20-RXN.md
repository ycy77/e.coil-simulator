---
entity_id: "reaction.ecocyc.5.1.3.20-RXN"
entity_type: "reaction"
name: "5.1.3.20-RXN"
source_database: "EcoCyc"
source_id: "5.1.3.20-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5.1.3.20-RXN

`reaction.ecocyc.5.1.3.20-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5.1.3.20-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP-D-GLYCERO-D-MANNO-HEPTOSE -> ADP-L-GLYCERO-D-MANNO-HEPTOSE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ADP-D-GLYCERO-D-MANNO-HEPTOSE -> ADP-L-GLYCERO-D-MANNO-HEPTOSE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ADP-L-glycero-D-mannoheptose 6-epimerase (complex.ecocyc.CPLX0-3681). Substrates: ADP-D-glycero-beta-D-manno-heptose (molecule.C06397). Products: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398).

## Enriched Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Annotation

ADP-D-GLYCERO-D-MANNO-HEPTOSE -> ADP-L-GLYCERO-D-MANNO-HEPTOSE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3681|complex.ecocyc.CPLX0-3681]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C06398|molecule.C06398]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06397|molecule.C06397]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00498|molecule.C00498]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:5.1.3.20-RXN`

## Notes

ADP-D-GLYCERO-D-MANNO-HEPTOSE -> ADP-L-GLYCERO-D-MANNO-HEPTOSE; direction=LEFT-TO-RIGHT
