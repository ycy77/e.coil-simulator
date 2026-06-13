---
entity_id: "gene.b3712"
entity_type: "gene"
name: "yieE"
source_database: "NCBI RefSeq"
source_id: "gene-b3712"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3712"
  - "yieE"
---

# yieE

`gene.b3712`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3712`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yieE (gene.b3712) is a gene entity. It encodes yieE (protein.P0ADM8). Encoded protein function: Uncharacterized protein YieE EcoCyc product frame: EG11722-MONOMER. Genomic coordinates: 3893881-3894630. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 22, 2016.

## Biological Role

Repressed by arcA (protein.P0A9Q1), nac (protein.Q47005). Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADM8|protein.P0ADM8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yieE; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yieE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yieE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012144,ECOCYC:EG11722,GeneID:948226`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3893881-3894630:+; feature_type=gene
