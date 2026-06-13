---
entity_id: "reaction.ecocyc.DTDPDEHYDRHAMEPIM-RXN"
entity_type: "reaction"
name: "DTDPDEHYDRHAMEPIM-RXN"
source_database: "EcoCyc"
source_id: "DTDPDEHYDRHAMEPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DTDPDEHYDRHAMEPIM-RXN

`reaction.ecocyc.DTDPDEHYDRHAMEPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DTDPDEHYDRHAMEPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the third step of dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide. EcoCyc reaction equation: DTDP-DEOH-DEOXY-GLUCOSE -> DTDP-DEOH-DEOXY-MANNOSE; direction=LEFT-TO-RIGHT. This reaction is the third step of dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide.

## Biological Role

Catalyzed by rfbC (protein.P37745). Substrates: dTDP-4-oxo-6-deoxy-D-glucose (molecule.C11907). Products: dTDP-4-dehydro-beta-L-rhamnose (molecule.C00688).

## Enriched Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)

## Annotation

This reaction is the third step of dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide.

## Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37745|protein.P37745]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00688|molecule.C00688]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C11907|molecule.C11907]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DTDPDEHYDRHAMEPIM-RXN`

## Notes

DTDP-DEOH-DEOXY-GLUCOSE -> DTDP-DEOH-DEOXY-MANNOSE; direction=LEFT-TO-RIGHT
