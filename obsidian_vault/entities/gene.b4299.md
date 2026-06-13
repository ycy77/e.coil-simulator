---
entity_id: "gene.b4299"
entity_type: "gene"
name: "yjhI"
source_database: "NCBI RefSeq"
source_id: "gene-b4299"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4299"
  - "yjhI"
---

# yjhI

`gene.b4299`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4299`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjhI (gene.b4299) is a gene entity. It encodes yjhI (protein.P39360). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YjhI EcoCyc product frame: G7912-MONOMER. Genomic coordinates: 4525015-4525803. EcoCyc protein note: Expression of the yjhIHG operon is inducible by D-xylonate . YjhI was predicted to be an IclR-type transcription factor . Genome-wide YjhI binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . It was proposed that YjhI is involved in transcriptional regulation of the energy conversion between pyruvate and glycolaldehyde based on annotated functions of their binding target genes identified by ChIP-exo studies.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39360|protein.P39360]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yjhI; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014092,ECOCYC:G7912,GeneID:949100`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4525015-4525803:-; feature_type=gene
