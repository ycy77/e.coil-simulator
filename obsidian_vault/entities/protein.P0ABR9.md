---
entity_id: "protein.P0ABR9"
entity_type: "protein"
name: "mhpB"
source_database: "UniProt"
source_id: "P0ABR9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpB b0348 JW0339"
---

# mhpB

`protein.P0ABR9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABR9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the non-heme iron(II)-dependent oxidative cleavage of 2,3-dihydroxyphenylpropionic acid and 2,3-dihydroxicinnamic acid into 2-hydroxy-6-ketononadienedioate and 2-hydroxy-6-ketononatrienedioate, respectively. {ECO:0000269|PubMed:8399388, ECO:0000269|PubMed:8752345}.

## Biological Role

Component of 3-carboxyethylcatechol 2,3-dioxygenase (complex.ecocyc.DHPDIOXYGEN-CPLX).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Catalyzes the non-heme iron(II)-dependent oxidative cleavage of 2,3-dihydroxyphenylpropionic acid and 2,3-dihydroxicinnamic acid into 2-hydroxy-6-ketononadienedioate and 2-hydroxy-6-ketononatrienedioate, respectively. {ECO:0000269|PubMed:8399388, ECO:0000269|PubMed:8752345}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DHPDIOXYGEN-CPLX|complex.ecocyc.DHPDIOXYGEN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0348|gene.b0348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABR9`
- `KEGG:ecj:JW0339;eco:b0348;ecoc:C3026_01715;ecoc:C3026_24875;`
- `GeneID:93777107;945047;`
- `GO:GO:0008198; GO:0019380; GO:0019622; GO:0046271; GO:0047070`
- `EC:1.13.11.16`

## Notes

2,3-dihydroxyphenylpropionate/2,3-dihydroxicinnamic acid 1,2-dioxygenase (EC 1.13.11.16) (3-carboxyethylcatechol 2,3-dioxygenase)
