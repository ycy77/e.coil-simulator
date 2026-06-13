---
entity_id: "gene.b2561"
entity_type: "gene"
name: "yfhH"
source_database: "NCBI RefSeq"
source_id: "gene-b2561"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2561"
  - "yfhH"
---

# yfhH

`gene.b2561`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2561`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfhH (gene.b2561) is a gene entity. It encodes yfhH (protein.P37767). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YfhH EcoCyc product frame: EG12308-MONOMER. Genomic coordinates: 2698759-2699607. EcoCyc protein note: YfhH, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the RipR family of transcription factors, and it was predicted to regulate genes related to metabolism . Upstream of the yfhH gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yfhH gene is affected by cold or heat stress . The YfhH binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37767|protein.P37767]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008428,ECOCYC:EG12308,GeneID:947030`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2698759-2699607:+; feature_type=gene
