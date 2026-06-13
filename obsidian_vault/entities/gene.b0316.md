---
entity_id: "gene.b0316"
entity_type: "gene"
name: "yahB"
source_database: "NCBI RefSeq"
source_id: "gene-b0316"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0316"
  - "yahB"
---

# yahB

`gene.b0316`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0316`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yahB (gene.b0316) is a gene entity. It encodes yahB (protein.P77700). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YahB EcoCyc product frame: G6181-MONOMER. Genomic coordinates: 333501-334433. EcoCyc protein note: YahB was predicted to be a LysR-type transcription factor , and it contains a helix-turn-helix motif to bind DNA in its N-terminal domain . YahB DNA-binding activity was probed in vivo in glucose M9 minimal medium through chromatin immunoprecipitation assays (ChIP-exo) . It was predicted to regulate genes related to metabolism . However, the effect of YahB on the transcription of any gene has not yet been demonstrated . The transcription of the yahB gene is affected by temperature and Fe2+ .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77700|protein.P77700]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001088,ECOCYC:G6181,GeneID:945278`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:333501-334433:-; feature_type=gene
