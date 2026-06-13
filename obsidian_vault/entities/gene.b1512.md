---
entity_id: "gene.b1512"
entity_type: "gene"
name: "lsrR"
source_database: "NCBI RefSeq"
source_id: "gene-b1512"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1512"
  - "lsrR"
---

# lsrR

`gene.b1512`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1512`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrR (gene.b1512) is a gene entity. It encodes lsrR (protein.P76141). Encoded protein function: FUNCTION: Transcriptional regulator that represses the expression of the lsr operon (lsrACDBFG-tam) in the absence of the quorum-sensing signaling molecule autoinducer 2 (AI-2) (PubMed:15743955, PubMed:16321939, PubMed:19636340). It also represses the expression of the lsrRK operon (PubMed:15743955, PubMed:16321939, PubMed:19636340). Acts by binding directly to the lsrA and lsrR promoter regions (PubMed:19636340). In the presence of phosphorylated autoinducer-2 (phospho-AI-2), LsrR is inactivated, leading to the transcription of the genes (PubMed:15743955, PubMed:16321939, PubMed:19636340). In addition to controlling the transcription of the lsr and lsrRK operons, LsrR may act as a global regulator that regulates the expression of a variety of genes, including genes involved in biofilm formation, host invasion and stress responses (PubMed:17557827). It also regulates the expression of several small RNAs (sRNAs), including DsrA (PubMed:17557827). {ECO:0000269|PubMed:15743955, ECO:0000269|PubMed:16321939, ECO:0000269|PubMed:17557827, ECO:0000269|PubMed:19636340}. EcoCyc product frame: G6799-MONOMER. EcoCyc synonyms: ydeW. Genomic coordinates: 1600288-1601241.

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76141|protein.P76141]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrR; function=+
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005045,ECOCYC:G6799,GeneID:946070`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1600288-1601241:-; feature_type=gene
