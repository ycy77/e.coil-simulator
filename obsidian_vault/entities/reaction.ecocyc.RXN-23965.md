---
entity_id: "reaction.ecocyc.RXN-23965"
entity_type: "reaction"
name: "RXN-23965"
source_database: "EcoCyc"
source_id: "RXN-23965"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23965

`reaction.ecocyc.RXN-23965`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23965`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPD-26488 -> CPD-13576 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD-26488 -> CPD-13576 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hydroxyethylthiazole kinase (complex.ecocyc.CPLX0-8211). Substrates: ATP (molecule.C00002), 5-(2-hydroxyethyl)-4-methyl-1,3-thiazole-2-carboxylate (molecule.ecocyc.CPD-26488). Products: ADP (molecule.C00008), H+ (molecule.C00080), 2-(2-Carboxy-4-methylthiazol-5-yl)ethyl phosphate (molecule.C20247).

## Enriched Pathways

- `ecocyc.PWY-8457` thiamine diphosphate salvage V (EcoCyc)

## Annotation

ATP + CPD-26488 -> CPD-13576 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8457` thiamine diphosphate salvage V (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8211|complex.ecocyc.CPLX0-8211]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20247|molecule.C20247]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26488|molecule.ecocyc.CPD-26488]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23965`

## Notes

ATP + CPD-26488 -> CPD-13576 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
