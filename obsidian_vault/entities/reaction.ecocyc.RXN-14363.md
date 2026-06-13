---
entity_id: "reaction.ecocyc.RXN-14363"
entity_type: "reaction"
name: "RXN-14363"
source_database: "EcoCyc"
source_id: "RXN-14363"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14363

`reaction.ecocyc.RXN-14363`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14363`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 + PROTON -> DIACYLGLYCEROL + CPD-15238; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 + PROTON -> DIACYLGLYCEROL + CPD-15238; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by eptC (protein.P0CB39). Substrates: H+ (molecule.C00080), Phosphatidylethanolamine (molecule.C00350), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359). Products: 1,2-Diacyl-sn-glycerol (molecule.C00641), lipid A-core oligosaccharide phosphoethanolamine (hep I) (molecule.ecocyc.CPD-15238).

## Annotation

L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 + PROTON -> DIACYLGLYCEROL + CPD-15238; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0CB39|protein.P0CB39]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15238|molecule.ecocyc.CPD-15238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14363`

## Notes

L-1-PHOSPHATIDYL-ETHANOLAMINE + CPD-21359 + PROTON -> DIACYLGLYCEROL + CPD-15238; direction=PHYSIOL-LEFT-TO-RIGHT
