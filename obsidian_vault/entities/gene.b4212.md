---
entity_id: "gene.b4212"
entity_type: "gene"
name: "ytfH"
source_database: "NCBI RefSeq"
source_id: "gene-b4212"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4212"
  - "ytfH"
---

# ytfH

`gene.b4212`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4212`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfH (gene.b4212) is a gene entity. It encodes ytfH (protein.P0ACN2). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YtfH EcoCyc product frame: G7869-MONOMER. Genomic coordinates: 4434113-4434493. EcoCyc protein note: YtfH, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the RipR family of transcription factors, and it was predicted to regulate genes related to metabolism . YtfH was mentioned as a predicted inner membrane protein that may be a substrate for the periplasmic chaperone YfgM . Upstream of the ytfH gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the ytfH gene is affected by heat stress, oxidative stress, and glucose-lactose shift . The YtfH binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACN2|protein.P0ACN2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013777,ECOCYC:G7869,GeneID:948730`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4434113-4434493:+; feature_type=gene
