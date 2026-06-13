---
entity_id: "protein.P0AAZ4"
entity_type: "protein"
name: "rarA"
source_database: "UniProt"
source_id: "P0AAZ4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rarA mgsA ycaJ b0892 JW0875"
---

# rarA

`protein.P0AAZ4`

## Static

- Type: `protein`
- Source: `UniProt:P0AAZ4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA-dependent ATPase that plays important roles in cellular responses to stalled DNA replication processes. {ECO:0000269|PubMed:11459952, ECO:0000269|PubMed:15743409, ECO:0000269|PubMed:21297161}.

## Biological Role

Component of replication-associated recombination protein A (complex.ecocyc.CPLX0-8560).

## Annotation

FUNCTION: DNA-dependent ATPase that plays important roles in cellular responses to stalled DNA replication processes. {ECO:0000269|PubMed:11459952, ECO:0000269|PubMed:15743409, ECO:0000269|PubMed:21297161}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8560|complex.ecocyc.CPLX0-8560]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0892|gene.b0892]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAZ4`
- `KEGG:ecj:JW0875;eco:b0892;ecoc:C3026_05520;`
- `GeneID:75170967;945505;`
- `GO:GO:0000731; GO:0003677; GO:0005524; GO:0006261; GO:0006310; GO:0008047; GO:0008094; GO:0016887; GO:0017116; GO:0030894; GO:0042802; GO:0051289`

## Notes

Replication-associated recombination protein A
