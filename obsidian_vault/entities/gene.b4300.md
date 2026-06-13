---
entity_id: "gene.b4300"
entity_type: "gene"
name: "sgcR"
source_database: "NCBI RefSeq"
source_id: "gene-b4300"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4300"
  - "sgcR"
---

# sgcR

`gene.b4300`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4300`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgcR (gene.b4300) is a gene entity. It encodes sgcR (protein.P39361). Encoded protein function: FUNCTION: Putative transcriptional regulator for the sgcREAQCX region. EcoCyc product frame: G7913-MONOMER. EcoCyc synonyms: yjhJ. Genomic coordinates: 4526106-4526888. EcoCyc protein note: SgcR, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, was predicted to regulate genes related to metabolism . Upstream of the sgcR gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the sgcR gene is affected by glucose-lactose shift and glucose-acetate shift . The SgcR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Biological Role

Repressed by slyA (protein.P0A8W2). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39361|protein.P39361]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgcR; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=sgcR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014094,ECOCYC:G7913,GeneID:946830`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4526106-4526888:-; feature_type=gene
