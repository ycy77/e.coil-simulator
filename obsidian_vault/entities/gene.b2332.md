---
entity_id: "gene.b2332"
entity_type: "gene"
name: "yfcO"
source_database: "NCBI RefSeq"
source_id: "gene-b2332"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2332"
  - "yfcO"
---

# yfcO

`gene.b2332`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2332`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfcO (gene.b2332) is a gene entity. It encodes yfcO (protein.P76498). Encoded protein function: FUNCTION: Part of the yfcOPQRSUV fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim genes. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G7203-MONOMER. Genomic coordinates: 2449228-2450049. EcoCyc protein note: YfcO is a hypothetical protein. Sequence similarity suggests that it is a member of the Outer Membrane Factor (OMF) family . yfcO is part of a putative chaperone-usher fimbrial operon . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yfcOPQRSTUV; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76498|protein.P76498]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfcO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfcO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007700,ECOCYC:G7203,GeneID:946620`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2449228-2450049:-; feature_type=gene
