---
entity_id: "gene.b1658"
entity_type: "gene"
name: "purR"
source_database: "NCBI RefSeq"
source_id: "gene-b1658"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1658"
  - "purR"
---

# purR

`gene.b1658`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1658`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purR (gene.b1658) is a gene entity. It encodes purR (protein.P0ACP7). Encoded protein function: FUNCTION: Is the main repressor of the genes involved in the de novo synthesis of purine nucleotides, regulating purB, purC, purEK, purF, purHD, purL, purMN and guaBA expression. In addition, it participates in the regulation or coregulation of genes involved in de novo pyrimidine nucleotide biosynthesis, salvage and uptake (pyrC, pyrD, carAB and codBA), and of several genes encoding enzymes necessary for nucleotide and polyamine biosynthesis (prsA, glyA, gcvTHP, speA, glnB). Binds to a 16-bp palindromic sequence located within the promoter region of pur regulon genes. The consensus binding sequence is 5'-ACGCAAACGTTTTCNT-3'. PurR is allosterically activated to bind its cognate DNA by binding the purine corepressors, hypoxanthine or guanine, thereby effecting transcription repression. {ECO:0000269|PubMed:1400170, ECO:0000269|PubMed:14741201, ECO:0000269|PubMed:2211500, ECO:0000269|PubMed:2404765}. EcoCyc product frame: PD00219. Genomic coordinates: 1737844-1738869.

## Biological Role

Repressed by sgrS (gene.b4577), purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACP7|protein.P0ACP7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=purR; function=+
- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=purR; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `C` - regulator=PurR; target=purR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005545,ECOCYC:EG10800,GeneID:945226`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1737844-1738869:+; feature_type=gene
