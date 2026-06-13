---
entity_id: "gene.b0034"
entity_type: "gene"
name: "caiF"
source_database: "NCBI RefSeq"
source_id: "gene-b0034"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0034"
  - "caiF"
---

# caiF

`gene.b0034`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0034`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

caiF (gene.b0034) is a gene entity. It encodes caiF (protein.P0AE58). Encoded protein function: FUNCTION: Potential transcriptional activator of carnitine metabolism. EcoCyc product frame: G6088-MONOMER. Genomic coordinates: 34300-34695.

## Biological Role

Repressed by nac (protein.Q47005). Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE58|protein.P0AE58]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=caiF; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=caiF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000125,ECOCYC:G6088,GeneID:944795`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:34300-34695:+; feature_type=gene
