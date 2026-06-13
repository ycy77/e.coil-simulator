---
entity_id: "gene.b1439"
entity_type: "gene"
name: "ydcR"
source_database: "NCBI RefSeq"
source_id: "gene-b1439"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1439"
  - "ydcR"
---

# ydcR

`gene.b1439`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1439`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcR (gene.b1439) is a gene entity. It encodes ydcR (protein.P77730). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YdcR EcoCyc product frame: G6750-MONOMER. Genomic coordinates: 1510003-1511409. EcoCyc protein note: YdcR is a member of the GntR family of transcriptional regulators . This family is known to be associated with regulation of carbon metabolism . YdcR has an HTH motif near its N terminus and an aminotransferase domain. YdcR DNA-binding activity was probed in vivo in glucose M9 minimal medium through chromatin immunoprecipitation assays (ChIP-exo) . However, the effect of YdcR on the transcription of any gene has not yet been demonstrated . The transcription of the ydcR gene is affected by UV, cadmium, and pH . The YdcR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . The YdcR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77730|protein.P77730]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004800,ECOCYC:G6750,GeneID:946004`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1510003-1511409:+; feature_type=gene
