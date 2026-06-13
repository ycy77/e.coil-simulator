---
entity_id: "protein.P76038"
entity_type: "protein"
name: "puuD"
source_database: "UniProt"
source_id: "P76038"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "puuD ycjL b1298 JW1291"
---

# puuD

`protein.P76038`

## Static

- Type: `protein`
- Source: `UniProt:P76038`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the breakdown of putrescine via hydrolysis of the gamma-glutamyl linkage of gamma-glutamyl-gamma-aminobutyrate. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:16499623}. PuuD was identified as the γ-glutamyl-γ-aminobutyrate hydrolase in a putrescine utilization pathway. The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . PuuD is highly expressed in early stationary phase; expression of puuD is induced by growth on putrescine as the sole source of nitrogen and during the transition of anaerobic to aerobic cultures . Addition of succinate or NH4Cl to the medium reduces PuuD expression . A strain carrying a mutation in puuD can not grow on putrescine as the sole source of nitrogen and accumulates γ-glutamyl-γ-aminobutyrate . PuuD: "putrescine utilization pathway" Review:

## Biological Role

Component of γ-glutamyl-γ-aminobutyrate hydrolase (complex.ecocyc.CPLX0-3943).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the breakdown of putrescine via hydrolysis of the gamma-glutamyl linkage of gamma-glutamyl-gamma-aminobutyrate. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:16499623}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3943|complex.ecocyc.CPLX0-3943]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1298|gene.b1298]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76038`
- `KEGG:ecj:JW1291;eco:b1298;`
- `GeneID:93775424;945882;`
- `GO:GO:0006598; GO:0009447; GO:0033969`
- `EC:3.5.1.94`

## Notes

Gamma-glutamyl-gamma-aminobutyrate hydrolase PuuD (Gamma-Glu-GABA hydrolase) (EC 3.5.1.94)
