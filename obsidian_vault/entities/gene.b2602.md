---
entity_id: "gene.b2602"
entity_type: "gene"
name: "yfiL"
source_database: "NCBI RefSeq"
source_id: "gene-b2602"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2602"
  - "yfiL"
---

# yfiL

`gene.b2602`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2602`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfiL (gene.b2602) is a gene entity. It encodes yfiL (protein.P11289). Encoded protein function: Uncharacterized protein YfiL (URF2) EcoCyc product frame: EG12446-MONOMER. Genomic coordinates: 2741360-2741725. EcoCyc protein note: YfiL is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Expression of yfiL is significantly decreased in populations adapted to the presence of ampicillin or tetracycline .

## Biological Role

Repressed by glaR (protein.P37338). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11289|protein.P11289]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfiL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfiL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008565,ECOCYC:EG12446,GeneID:947106`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2741360-2741725:+; feature_type=gene
