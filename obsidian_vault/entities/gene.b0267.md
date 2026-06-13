---
entity_id: "gene.b0267"
entity_type: "gene"
name: "yagA"
source_database: "NCBI RefSeq"
source_id: "gene-b0267"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0267"
  - "yagA"
---

# yagA

`gene.b0267`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0267`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagA (gene.b0267) is a gene entity. It encodes yagA (protein.P37007). Encoded protein function: Uncharacterized protein YagA EcoCyc product frame: EG12338-MONOMER. Genomic coordinates: 280829-281983. EcoCyc protein note: YagA, which is predicted to be a transcription factor, appears to belong to the RutR family, and it was predicted to regulate genes related to metabolism . Upstream of the yagA gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yagA gene is affected by stress and by conditions that lead to biofilm formation .

## Biological Role

Repressed by xynR (protein.P77300).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37007|protein.P37007]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77300|protein.P77300]] `RegulonDB` `C` - regulator=XynR; target=yagA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000915,ECOCYC:EG12338,GeneID:944937`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:280829-281983:-; feature_type=gene
