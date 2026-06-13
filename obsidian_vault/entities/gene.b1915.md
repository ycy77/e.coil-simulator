---
entity_id: "gene.b1915"
entity_type: "gene"
name: "yecF"
source_database: "NCBI RefSeq"
source_id: "gene-b1915"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1915"
  - "yecF"
---

# yecF

`gene.b1915`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1915`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yecF (gene.b1915) is a gene entity. It encodes yecF (protein.P0AD07). Encoded protein function: Uncharacterized protein YecF EcoCyc product frame: EG12861-MONOMER. Genomic coordinates: 1995818-1996042. EcoCyc protein note: The promoter of yecF is predicted to be σ28-dependent and can be transcribed by CPLX0-222 in vitro . Transcription of yecF is not activated by sdiA overexpression .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD07|protein.P0AD07]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yecF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006379,ECOCYC:EG12861,GeneID:946420`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1995818-1996042:+; feature_type=gene
