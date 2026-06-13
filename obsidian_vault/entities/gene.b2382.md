---
entity_id: "gene.b2382"
entity_type: "gene"
name: "ypdC"
source_database: "NCBI RefSeq"
source_id: "gene-b2382"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2382"
  - "ypdC"
---

# ypdC

`gene.b2382`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2382`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ypdC (gene.b2382) is a gene entity. It encodes ypdC (protein.P77396). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YpdC EcoCyc product frame: G7245-MONOMER. Genomic coordinates: 2501130-2501987. EcoCyc protein note: YpdC contains a predicted C-terminal AraC-type DNA-binding domain . It was predicted that this protein regulates genes related to metabolism . Upstream of the ypdC gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the ypdC gene is affected by conditions that lead to biofilm formation . The YpdC binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77396|protein.P77396]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ypdC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007859,ECOCYC:G7245,GeneID:946856`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2501130-2501987:+; feature_type=gene
