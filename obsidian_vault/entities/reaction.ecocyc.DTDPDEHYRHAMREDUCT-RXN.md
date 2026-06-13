---
entity_id: "reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN"
entity_type: "reaction"
name: "DTDPDEHYRHAMREDUCT-RXN"
source_database: "EcoCyc"
source_id: "DTDPDEHYRHAMREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DTDPDEHYRHAMREDUCT-RXN

`reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DTDPDEHYRHAMREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the fourth stp in the synthesis of dTDP-rhamnose (=dTDP-6-deoxy-L-mannose), a component of the O-antigen of lipopolysaccharide. EcoCyc reaction equation: NADP + DTDP-RHAMNOSE -> PROTON + NADPH + DTDP-DEOH-DEOXY-MANNOSE; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is the fourth stp in the synthesis of dTDP-rhamnose (=dTDP-6-deoxy-L-mannose), a component of the O-antigen of lipopolysaccharide.

## Biological Role

Catalyzed by rfbD (protein.P37760). Substrates: NADP+ (molecule.C00006), dTDP-L-rhamnose (molecule.C03319). Products: NADPH (molecule.C00005), H+ (molecule.C00080), dTDP-4-dehydro-beta-L-rhamnose (molecule.C00688).

## Enriched Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)

## Annotation

This reaction is the fourth stp in the synthesis of dTDP-rhamnose (=dTDP-6-deoxy-L-mannose), a component of the O-antigen of lipopolysaccharide.

## Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37760|protein.P37760]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00688|molecule.C00688]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03319|molecule.C03319]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DTDPDEHYRHAMREDUCT-RXN`

## Notes

NADP + DTDP-RHAMNOSE -> PROTON + NADPH + DTDP-DEOH-DEOXY-MANNOSE; direction=PHYSIOL-RIGHT-TO-LEFT
