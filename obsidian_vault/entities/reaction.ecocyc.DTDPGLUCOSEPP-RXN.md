---
entity_id: "reaction.ecocyc.DTDPGLUCOSEPP-RXN"
entity_type: "reaction"
name: "DTDPGLUCOSEPP-RXN"
source_database: "EcoCyc"
source_id: "DTDPGLUCOSEPP-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DTDPGLUCOSEPP-RXN

`reaction.ecocyc.DTDPGLUCOSEPP-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DTDPGLUCOSEPP-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the first reaction in dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide. EcoCyc reaction equation: PROTON + GLC-1-P + TTP -> DTDP-D-GLUCOSE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the first reaction in dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide.

## Biological Role

Catalyzed by glucose-1-phosphate thymidylyltransferase 2 (complex.ecocyc.CPLX0-8012), glucose-1-phosphate thymidylyltransferase 1 (complex.ecocyc.CPLX0-8034). Substrates: H+ (molecule.C00080), dTTP (molecule.C00459), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P). Products: Diphosphate (molecule.C00013), dTDP-glucose (molecule.C00842).

## Enriched Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)
- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Annotation

This reaction is the first reaction in dTDP-rhamnose biosynthesis, a component of the O-antigen of lipopolysaccharide.

## Pathways

- `ecocyc.DTDPRHAMSYN-PWY` dTDP-L-rhamnose biosynthesis (EcoCyc)
- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8012|complex.ecocyc.CPLX0-8012]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8034|complex.ecocyc.CPLX0-8034]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00842|molecule.C00842]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00842|molecule.C00842]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03319|molecule.C03319]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DTDPGLUCOSEPP-RXN`

## Notes

PROTON + GLC-1-P + TTP -> DTDP-D-GLUCOSE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
