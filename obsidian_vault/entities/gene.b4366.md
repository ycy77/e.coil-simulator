---
entity_id: "gene.b4366"
entity_type: "gene"
name: "bglJ"
source_database: "NCBI RefSeq"
source_id: "gene-b4366"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4366"
  - "bglJ"
---

# bglJ

`gene.b4366`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4366`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bglJ (gene.b4366) is a gene entity. It encodes bglJ (protein.P39404). Encoded protein function: FUNCTION: A crytic transcriptional activator. When its expression is induced it relieves H-NS repression of the bgl operon. Acts independently of transcription factor LeuO. {ECO:0000269|PubMed:8725214}. EcoCyc product frame: G7948-MONOMER. EcoCyc synonyms: yjjR. Genomic coordinates: 4604160-4604837. EcoCyc protein note: BglJ is a positive DNA-binding transcriptional regulator of transport and utilization of the aromatic β-glucosides arbutin and salicin . The expression of the gene bglJ induces the bglGFB operon via unknown mechanisms. This suggests the possibility that BglJ controls, directly or indirectly, the expression of the bgl operon . BglJ is a protein that belongs to the LuxR/UhpA family of transcriptional regulators . It shows a potential helix-turn-helix motif in the carboxyl-terminal domain, which has 48% identity and 70% similarity to the corresponding domain of the RcsB protein . A negative correlation between cellular growth and the copy number of the proteins BglJ has been reported . BglJ was transcriptionally upregulated in iron limitation over iron excess at 21% and 63% of dissolved oxygen as determined by RNA-seq .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), hns (protein.P0ACF8). Activated by leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39404|protein.P39404]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=bglJ; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=bglJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014324,ECOCYC:G7948,GeneID:948889`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4604160-4604837:+; feature_type=gene
