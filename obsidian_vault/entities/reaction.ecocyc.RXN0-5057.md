---
entity_id: "reaction.ecocyc.RXN0-5057"
entity_type: "reaction"
name: "RXN0-5057"
source_database: "EcoCyc"
source_id: "RXN0-5057"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5057

`reaction.ecocyc.RXN0-5057`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5057`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

KDO2-LIPID-IVA + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + HEPTOSYL-KDO2-LIPID-IVA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: KDO2-LIPID-IVA + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + HEPTOSYL-KDO2-LIPID-IVA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaC (protein.P24173). Substrates: KDO2-lipid IVA (molecule.C06025), ADP-L-glycero-beta-D-manno-heptose (molecule.C06398). Products: ADP (molecule.C00008), H+ (molecule.C00080), heptosyl-Kdo2-lipid IVA (molecule.ecocyc.HEPTOSYL-KDO2-LIPID-IVA).

## Annotation

KDO2-LIPID-IVA + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + HEPTOSYL-KDO2-LIPID-IVA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P24173|protein.P24173]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.HEPTOSYL-KDO2-LIPID-IVA|molecule.ecocyc.HEPTOSYL-KDO2-LIPID-IVA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5057`

## Notes

KDO2-LIPID-IVA + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + HEPTOSYL-KDO2-LIPID-IVA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
