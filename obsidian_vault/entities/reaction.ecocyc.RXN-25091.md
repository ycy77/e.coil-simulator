---
entity_id: "reaction.ecocyc.RXN-25091"
entity_type: "reaction"
name: "RXN-25091"
source_database: "EcoCyc"
source_id: "RXN-25091"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25091

`reaction.ecocyc.RXN-25091`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25091`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

IscU-2Fe2S+2 + Apo-FeS-cluster-proteins + ATP + WATER -> IscU + 2Fe-2S-proteins + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: IscU-2Fe2S+2 + Apo-FeS-cluster-proteins + ATP + WATER -> IscU + 2Fe-2S-proteins + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by [Fe-S] cluster biosynthesis chaperone/co-chaperone system (complex.ecocyc.CPLX0-12620). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-8566` [2Fe-2S] iron-sulfur cluster biosynthesis (bacterial IscS system) (EcoCyc)

## Annotation

IscU-2Fe2S+2 + Apo-FeS-cluster-proteins + ATP + WATER -> IscU + 2Fe-2S-proteins + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8566` [2Fe-2S] iron-sulfur cluster biosynthesis (bacterial IscS system) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12620|complex.ecocyc.CPLX0-12620]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25091`

## Notes

IscU-2Fe2S+2 + Apo-FeS-cluster-proteins + ATP + WATER -> IscU + 2Fe-2S-proteins + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
