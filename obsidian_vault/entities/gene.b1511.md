---
entity_id: "gene.b1511"
entity_type: "gene"
name: "lsrK"
source_database: "NCBI RefSeq"
source_id: "gene-b1511"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1511"
  - "lsrK"
---

# lsrK

`gene.b1511`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1511`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrK (gene.b1511) is a gene entity. It encodes lsrK (protein.P77432). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of autoinducer-2 (AI-2) to phospho-AI-2, which subsequently inactivates the transcriptional regulator LsrR and leads to the transcription of the lsr operon. Phosphorylates the ring-open form of (S)-4,5-dihydroxypentane-2,3-dione (DPD), which is the precursor to all AI-2 signaling molecules, at the C5 position. Required for the regulation of the lsr operon and many other genes. {ECO:0000269|PubMed:15601708, ECO:0000269|PubMed:17557827, ECO:0000269|PubMed:20025244}. EcoCyc product frame: G6798-MONOMER. EcoCyc synonyms: ydeV. Genomic coordinates: 1598617-1600209. EcoCyc protein note: LsrK is a kinase that is able to phosphorylate the quorum-sensing autoinducer molecule AI-2 . Based on its similarity to LsrK from Salmonella typhimurium, LsrK was already predicted to have AI-2 kinase activity . Phosphorylation of AI-2 by LsrK is essential for internalization and sequestration of AI-2 . Kinetic analysis of LsrK from Salmonella was most consistent with a rapid equilibrium ordered reaction mechanism with ATP binding first . LsrK has been overexpressed and crystallized . LsrK copurifies with PTSH-MONOMER, and co-crystal structures have been solved; LsrK domain I binds HPr, and domain II binds ATP...

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77432|protein.P77432]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrK; function=+
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005041,ECOCYC:G6798,GeneID:946069`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1598617-1600209:-; feature_type=gene
