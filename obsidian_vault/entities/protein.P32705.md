---
entity_id: "protein.P32705"
entity_type: "protein"
name: "actP"
source_database: "UniProt"
source_id: "P32705"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "actP yjcG b4067 JW4028"
---

# actP

`protein.P32705`

## Static

- Type: `protein`
- Source: `UniProt:P32705`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Transports acetate. Also able to transport glycolate. {ECO:0000269|PubMed:14563880}.

## Biological Role

Component of acetate/glycolate:cation symporter (complex.ecocyc.CPLX0-7955).

## Annotation

FUNCTION: Transports acetate. Also able to transport glycolate. {ECO:0000269|PubMed:14563880}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7955|complex.ecocyc.CPLX0-7955]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4067|gene.b4067]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32705`
- `KEGG:ecj:JW4028;eco:b4067;ecoc:C3026_21975;`
- `GeneID:948575;`
- `GO:GO:0005886; GO:0006814; GO:0006847; GO:0015123; GO:0015293; GO:0015654; GO:0015710; GO:0043879`

## Notes

Cation/acetate symporter ActP (Acetate permease) (Acetate transporter ActP)
