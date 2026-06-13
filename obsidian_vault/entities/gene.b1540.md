---
entity_id: "gene.b1540"
entity_type: "gene"
name: "rspR"
source_database: "NCBI RefSeq"
source_id: "gene-b1540"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1540"
  - "rspR"
---

# rspR

`gene.b1540`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1540`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rspR (gene.b1540) is a gene entity. It encodes rspR (protein.P0ACM2). Encoded protein function: FUNCTION: Repressor of the rspAB operon. Acts by binding directly to the upstream region of rspA. {ECO:0000269|PubMed:22972332}. EcoCyc product frame: G6814-MONOMER. EcoCyc synonyms: ydfH. Genomic coordinates: 1628352-1629038. EcoCyc protein note: YdfH belongs to the GntR transcription factor family , for which the consensus sequence is reported to be tnGTnnnACna . Although only one site was determined in a gel shift assay, it is possible that YfdH binds as a complex of flanking regions of the core sequence (-65 to -50) . It was determined by Genomic SELEX screening that a site located upstream of rspAB is the only target of RspR . The RspR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Biological Role

Activated by phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACM2|protein.P0ACM2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=rspR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005144,ECOCYC:G6814,GeneID:946087`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1628352-1629038:+; feature_type=gene
