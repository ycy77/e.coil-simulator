---
entity_id: "gene.b4192"
entity_type: "gene"
name: "ulaG"
source_database: "NCBI RefSeq"
source_id: "gene-b4192"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4192"
  - "ulaG"
---

# ulaG

`gene.b4192`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4192`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaG (gene.b4192) is a gene entity. It encodes ulaG (protein.P39300). Encoded protein function: FUNCTION: Probably catalyzes the hydrolysis of L-ascorbate-6-P into 3-keto-L-gulonate-6-P. Is essential for L-ascorbate utilization under anaerobic conditions. Also shows phosphodiesterase activity, hydrolyzing phosphodiester bond in the artificial chromogenic substrate bis-p-nitrophenyl phosphate (bis-pNPP). {ECO:0000269|PubMed:12644495, ECO:0000269|PubMed:15808744}. EcoCyc product frame: G7855-MONOMER. EcoCyc synonyms: yjfR. Genomic coordinates: 4418561-4419625.

## Biological Role

Repressed by ulaR (protein.P0A9W0).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39300|protein.P39300]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9W0|protein.P0A9W0]] `RegulonDB` `S` - regulator=UlaR; target=ulaG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013717,ECOCYC:G7855,GeneID:948705`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4418561-4419625:-; feature_type=gene
