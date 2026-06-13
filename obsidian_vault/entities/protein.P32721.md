---
entity_id: "protein.P32721"
entity_type: "protein"
name: "alsA"
source_database: "UniProt"
source_id: "P32721"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alsA yjcW b4087 JW4048"
---

# alsA

`protein.P32721`

## Static

- Type: `protein`
- Source: `UniProt:P32721`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex AlsBAC involved in D-allose import. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:9401019}. alsA encodes the predicted ATP binding subunit of a D-allose ABC transporter . alsA contains fused ATP-binding cassette domains (ABC-ABC)

## Biological Role

Component of D-allose ABC transporter (complex.ecocyc.ABC-42-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex AlsBAC involved in D-allose import. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:9401019}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-42-CPLX|complex.ecocyc.ABC-42-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4087|gene.b4087]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32721`
- `KEGG:ecj:JW4048;eco:b4087;ecoc:C3026_22095;`
- `GeneID:948593;`
- `GO:GO:0005524; GO:0005886; GO:0015147; GO:0015615; GO:0015752; GO:0015754; GO:0016020; GO:0016887; GO:0055052`
- `EC:7.5.2.8`

## Notes

D-allose import ATP-binding protein AlsA (EC 7.5.2.8)
