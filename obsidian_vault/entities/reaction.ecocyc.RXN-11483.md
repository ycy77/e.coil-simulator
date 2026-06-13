---
entity_id: "reaction.ecocyc.RXN-11483"
entity_type: "reaction"
name: "RXN-11483"
source_database: "EcoCyc"
source_id: "RXN-11483"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11483

`reaction.ecocyc.RXN-11483`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11483`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pimeloyl-ACP-methyl-esters + WATER -> Pimeloyl-ACPs + METOH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Pimeloyl-ACP-methyl-esters + WATER -> Pimeloyl-ACPs + METOH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bioH (protein.P13001). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), Methanol (molecule.C00132).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

Pimeloyl-ACP-methyl-esters + WATER -> Pimeloyl-ACPs + METOH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P13001|protein.P13001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00132|molecule.C00132]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11483`

## Notes

Pimeloyl-ACP-methyl-esters + WATER -> Pimeloyl-ACPs + METOH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
