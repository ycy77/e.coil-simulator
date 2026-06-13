---
entity_id: "gene.b1361"
entity_type: "gene"
name: "ydaW"
source_database: "NCBI RefSeq"
source_id: "gene-b1361"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1361"
  - "ydaW"
---

# ydaW

`gene.b1361`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1361`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydaW (gene.b1361) is a gene entity. It encodes ydaW (protein.P76066). Encoded protein function: Protein YdaW EcoCyc product frame: G6685-MONOMER. Genomic coordinates: 1422752-1423312. EcoCyc protein note: YdaW appears to belong to the MarR family of transcription factors . The transcription of the ydaW gene is affected under conditions that lead to biofilm formation and during UV exposure .

## Biological Role

Repressed by racR (protein.P76062).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76066|protein.P76066]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P76062|protein.P76062]] `RegulonDB` `S` - regulator=RacR; target=ydaW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004562,ECOCYC:G6685,GeneID:945927`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1422752-1423312:+; feature_type=gene
