---
entity_id: "protein.P77795"
entity_type: "protein"
name: "ydcT"
source_database: "UniProt"
source_id: "P77795"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydcT b1441 JW1436"
---

# ydcT

`protein.P77795`

## Static

- Type: `protein`
- Source: `UniProt:P77795`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably part of the ABC transporter complex YdcSTUV. Probably responsible for energy coupling to the transport system. {ECO:0000305}. YdcT is the predicted ATP-binding component of an uncharacterized ABC transporter .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-51-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Probably part of the ABC transporter complex YdcSTUV. Probably responsible for energy coupling to the transport system. {ECO:0000305}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-51-CPLX|complex.ecocyc.ABC-51-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1441|gene.b1441]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77795`
- `KEGG:ecj:JW1436;eco:b1441;ecoc:C3026_08385;`
- `GeneID:946007;`
- `GO:GO:0005524; GO:0005886; GO:0015417; GO:0015847; GO:0016020; GO:0016887; GO:0055052; GO:0055085`

## Notes

Uncharacterized ABC transporter ATP-binding protein YdcT
