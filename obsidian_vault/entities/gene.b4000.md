---
entity_id: "gene.b4000"
entity_type: "gene"
name: "hupA"
source_database: "NCBI RefSeq"
source_id: "gene-b4000"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4000"
  - "hupA"
---

# hupA

`gene.b4000`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4000`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hupA (gene.b4000) is a gene entity. It encodes hupA (protein.P0ACF0). Encoded protein function: FUNCTION: Histone-like DNA-binding protein which is capable of wrapping DNA to stabilize it, and thus to prevent its denaturation under extreme environmental conditions. {ECO:0000305|PubMed:24916461}. EcoCyc product frame: EG10466-MONOMER. Genomic coordinates: 4200281-4200553.

## Biological Role

Activated by fis (protein.P0A6R3), crp (protein.P0ACJ8), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACF0|protein.P0ACF0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=hupA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hupA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hupA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013077,ECOCYC:EG10466,GeneID:948499`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4200281-4200553:+; feature_type=gene
