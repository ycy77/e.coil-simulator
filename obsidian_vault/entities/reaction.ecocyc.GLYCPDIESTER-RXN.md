---
entity_id: "reaction.ecocyc.GLYCPDIESTER-RXN"
entity_type: "reaction"
name: "GLYCPDIESTER-RXN"
source_database: "EcoCyc"
source_id: "GLYCPDIESTER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCPDIESTER-RXN

`reaction.ecocyc.GLYCPDIESTER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCPDIESTER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of metabolism of glycerophospholipids. EcoCyc reaction equation: Glycerophosphodiesters + WATER -> Alcohols + GLYCEROL-3P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of metabolism of glycerophospholipids.

## Biological Role

Catalyzed by glycerophosphoryl diester phosphodiesterase, periplasmic (complex.ecocyc.GLYCPDIESTER-PERI-CPLX), ugpQ (protein.P10908). Substrates: H2O (molecule.C00001), an sn-glycerophosphodiester (molecule.ecocyc.Glycerophosphodiesters). Products: H+ (molecule.C00080), sn-Glycerol 3-phosphate (molecule.C00093), an alcohol (molecule.ecocyc.Alcohols).

## Enriched Pathways

- `ecocyc.PWY-6952` glycerophosphodiester degradation (EcoCyc)

## Annotation

This reaction is part of metabolism of glycerophospholipids.

## Pathways

- `ecocyc.PWY-6952` glycerophosphodiester degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.GLYCPDIESTER-PERI-CPLX|complex.ecocyc.GLYCPDIESTER-PERI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P10908|protein.P10908]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Glycerophosphodiesters|molecule.ecocyc.Glycerophosphodiesters]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLYCPDIESTER-RXN`

## Notes

Glycerophosphodiesters + WATER -> Alcohols + GLYCEROL-3P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
