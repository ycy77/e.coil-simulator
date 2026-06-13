---
entity_id: "gene.b2577"
entity_type: "gene"
name: "yfiE"
source_database: "NCBI RefSeq"
source_id: "gene-b2577"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2577"
  - "yfiE"
---

# yfiE

`gene.b2577`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2577`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfiE (gene.b2577) is a gene entity. It encodes yfiE (protein.P33634). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YfiE EcoCyc product frame: EG11785-MONOMER. Genomic coordinates: 2714439-2715320. EcoCyc protein note: YfiE contains a helix-turn-helix motif to bind DNA in its N-terminal domain and it was predicted that this protein regulates genes related to cysteine and O-acetylserine export and HOCl resistance . Genome-wide YfiE binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . Upstream of the yfiE gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yfiE gene is affected by cadmium and conditions that lead to biofilm formation . The YfiE binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33634|protein.P33634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008483,ECOCYC:EG11785,GeneID:947064`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2714439-2715320:-; feature_type=gene
