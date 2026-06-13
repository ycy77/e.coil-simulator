---
entity_id: "reaction.ecocyc.RXN0-4581"
entity_type: "reaction"
name: "RXN0-4581"
source_database: "EcoCyc"
source_id: "RXN0-4581"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4581

`reaction.ecocyc.RXN0-4581`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4581`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

L-1-PHOSPHATIDYL-ETHANOLAMINE + KDO2-LIPID-IVA -> DIACYLGLYCEROL + PHOSPHATIDYLETHANOLAMINE-KDO2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-1-PHOSPHATIDYL-ETHANOLAMINE + KDO2-LIPID-IVA -> DIACYLGLYCEROL + PHOSPHATIDYLETHANOLAMINE-KDO2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by eptB (protein.P37661). Substrates: Phosphatidylethanolamine (molecule.C00350), KDO2-lipid IVA (molecule.C06025). Products: 1,2-Diacyl-sn-glycerol (molecule.C00641), 7-O-[2-aminoethoxy(hydroxy)phosphoryl]-α-D-Kdo-(2→4)-α-D-Kdo-(2→6)-lipid IVA (molecule.ecocyc.PHOSPHATIDYLETHANOLAMINE-KDO2).

## Annotation

L-1-PHOSPHATIDYL-ETHANOLAMINE + KDO2-LIPID-IVA -> DIACYLGLYCEROL + PHOSPHATIDYLETHANOLAMINE-KDO2; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37661|protein.P37661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PHOSPHATIDYLETHANOLAMINE-KDO2|molecule.ecocyc.PHOSPHATIDYLETHANOLAMINE-KDO2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4581`

## Notes

L-1-PHOSPHATIDYL-ETHANOLAMINE + KDO2-LIPID-IVA -> DIACYLGLYCEROL + PHOSPHATIDYLETHANOLAMINE-KDO2; direction=PHYSIOL-LEFT-TO-RIGHT
