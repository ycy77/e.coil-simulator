---
entity_id: "protein.P0ADQ2"
entity_type: "protein"
name: "fabY"
source_database: "UniProt"
source_id: "P0ADQ2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabY yiiD b3888 JW3859"
---

# fabY

`protein.P0ADQ2`

## Static

- Type: `protein`
- Source: `UniProt:P0ADQ2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Supports initiation of fatty acid biosynthesis in the absence of FabH. {ECO:0000269|PubMed:31331975}.

## Biological Role

Component of malonyl-ACP decarboxylase (complex.ecocyc.CPLX0-12386).

## Annotation

FUNCTION: Supports initiation of fatty acid biosynthesis in the absence of FabH. {ECO:0000269|PubMed:31331975}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12386|complex.ecocyc.CPLX0-12386]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3888|gene.b3888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADQ2`
- `KEGG:ecj:JW3859;eco:b3888;`
- `GeneID:948387;`
- `GO:GO:0006633; GO:0016747; GO:0050080`
- `EC:2.3.1.-`

## Notes

Probable acyltransferase FabY (EC 2.3.1.-)
