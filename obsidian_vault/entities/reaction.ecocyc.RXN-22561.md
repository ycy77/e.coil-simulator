---
entity_id: "reaction.ecocyc.RXN-22561"
entity_type: "reaction"
name: "RXN-22561"
source_database: "EcoCyc"
source_id: "RXN-22561"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22561

`reaction.ecocyc.RXN-22561`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22561`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 -> DIACYLGLYCEROL + CPD-24804; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 -> DIACYLGLYCEROL + CPD-24804; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by eptB (protein.P37661). Substrates: Phosphatidylethanolamine (molecule.C00350), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359). Products: 1,2-Diacyl-sn-glycerol (molecule.C00641), lipid A-core oligosaccharide phosphoethanolamine (KdoII) (molecule.ecocyc.CPD-24804).

## Annotation

L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 -> DIACYLGLYCEROL + CPD-24804; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37661|protein.P37661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24804|molecule.ecocyc.CPD-24804]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22561`

## Notes

L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 -> DIACYLGLYCEROL + CPD-24804; direction=PHYSIOL-LEFT-TO-RIGHT
