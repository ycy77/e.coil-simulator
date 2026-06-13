---
entity_id: "reaction.ecocyc.RXN-11326"
entity_type: "reaction"
name: "(KDO)3-lipid IVA (2->4) 3-deoxy-D-manno-octulosonic acid transferase"
source_database: "EcoCyc"
source_id: "RXN-11326"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# (KDO)3-lipid IVA (2->4) 3-deoxy-D-manno-octulosonic acid transferase

`reaction.ecocyc.RXN-11326`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11326`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

KDO2-LIPID-IVA + CMP-KDO -> CPD-12284 + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: KDO2-LIPID-IVA + CMP-KDO -> CPD-12284 + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaZ (protein.P27241). Substrates: CMP-3-deoxy-D-manno-octulosonate (molecule.C04121), KDO2-lipid IVA (molecule.C06025). Products: CMP (molecule.C00055), H+ (molecule.C00080), α-Kdo-(2->4)-α-Kdo-(2->4)-α-Kdo-(2->6)-lipid IVA (E. coli) (molecule.ecocyc.CPD-12284).

## Annotation

KDO2-LIPID-IVA + CMP-KDO -> CPD-12284 + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27241|protein.P27241]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12284|molecule.ecocyc.CPD-12284]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04121|molecule.C04121]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11326`

## Notes

KDO2-LIPID-IVA + CMP-KDO -> CPD-12284 + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
