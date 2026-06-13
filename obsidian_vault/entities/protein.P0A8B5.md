---
entity_id: "protein.P0A8B5"
entity_type: "protein"
name: "ybaB"
source_database: "UniProt"
source_id: "P0A8B5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000255|HAMAP-Rule:MF_00274}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybaB b0471 JW0460"
---

# ybaB

`protein.P0A8B5`

## Static

- Type: `protein`
- Source: `UniProt:P0A8B5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000255|HAMAP-Rule:MF_00274}.

## Enriched Summary

FUNCTION: Binds to DNA and alters its conformation. May be involved in regulation of gene expression, nucleoid organization and DNA protection. {ECO:0000255|HAMAP-Rule:MF_00274}.

## Biological Role

Component of putative nucleoid-associated protein YbaB (complex.ecocyc.CPLX0-7816).

## Annotation

FUNCTION: Binds to DNA and alters its conformation. May be involved in regulation of gene expression, nucleoid organization and DNA protection. {ECO:0000255|HAMAP-Rule:MF_00274}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7816|complex.ecocyc.CPLX0-7816]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0471|gene.b0471]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8B5`
- `KEGG:ecj:JW0460;eco:b0471;ecoc:C3026_02315;`
- `GeneID:44979459;945104;`
- `GO:GO:0003677; GO:0005829; GO:0006950; GO:0009314; GO:0043590`

## Notes

Nucleoid-associated protein YbaB
