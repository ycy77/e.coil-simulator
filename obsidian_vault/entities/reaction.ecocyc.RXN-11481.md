---
entity_id: "reaction.ecocyc.RXN-11481"
entity_type: "reaction"
name: "RXN-11481"
source_database: "EcoCyc"
source_id: "RXN-11481"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11481

`reaction.ecocyc.RXN-11481`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11481`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-hydroxypimeloyl-ACP-methyl-esters -> Enoylpimeloyl-ACP-methyl-esters + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 3-hydroxypimeloyl-ACP-methyl-esters -> Enoylpimeloyl-ACP-methyl-esters + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase (complex.ecocyc.FABZ-CPLX). Products: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

3-hydroxypimeloyl-ACP-methyl-esters -> Enoylpimeloyl-ACP-methyl-esters + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.FABZ-CPLX|complex.ecocyc.FABZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN-11481`

## Notes

3-hydroxypimeloyl-ACP-methyl-esters -> Enoylpimeloyl-ACP-methyl-esters + WATER; direction=LEFT-TO-RIGHT
