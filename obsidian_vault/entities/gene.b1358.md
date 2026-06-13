---
entity_id: "gene.b1358"
entity_type: "gene"
name: "ydaT"
source_database: "NCBI RefSeq"
source_id: "gene-b1358"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1358"
  - "ydaT"
---

# ydaT

`gene.b1358`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1358`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydaT (gene.b1358) is a gene entity. It encodes ydaT (protein.P76064). Encoded protein function: FUNCTION: Transcriptional regulator that causes a severe detrimental growth effect and reduces cell viability (PubMed:38153127). When expressed, it alters expression of a variety of bacterial regulons normally controlled by the transcriptional regulatory protein RcsA, resulting in deficient lipopolysaccharide biosynthesis and cell division (PubMed:38153127). YdaT has no effect on Rac prophage excision (PubMed:38153127). Overexpression of ydaST reduces growth and leads to loss of cell viability (PubMed:29205228). May contribute to toxicity and morphological defects (PubMed:29205229). {ECO:0000269|PubMed:29205228, ECO:0000269|PubMed:29205229, ECO:0000269|PubMed:38153127}. EcoCyc product frame: G6682-MONOMER. Genomic coordinates: 1420684-1421106. EcoCyc protein note: This Rac prophage G6682 gene was first identified in TAX-562 K-12 as a putative homolog of the λ phage cII lysogenic regulatory gene and is next to G6681, possibly as part of the same operon . YdaT appears to regulate lipopolysaccharide biosynthesis and cell division genes . The ydaST locus was computationally predicted to encode a toxin/antitoxin (TA) pair . However, no evidence for this function was found in a study aimed at validating and characterizing new TA loci in E. coli K-12...

## Biological Role

Repressed by racR (protein.P76062), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76064|protein.P76064]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P76062|protein.P76062]] `RegulonDB` `S` - regulator=RacR; target=ydaT; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydaT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004556,ECOCYC:G6682,GeneID:945924`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1420684-1421106:+; feature_type=gene
