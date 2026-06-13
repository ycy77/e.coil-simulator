---
entity_id: "gene.b0704"
entity_type: "gene"
name: "ybfC"
source_database: "NCBI RefSeq"
source_id: "gene-b0704"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0704"
  - "ybfC"
---

# ybfC

`gene.b0704`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0704`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybfC (gene.b0704) is a gene entity. It encodes ybfC (protein.P28915). Encoded protein function: Uncharacterized protein YbfC EcoCyc product frame: EG11523-MONOMER. Genomic coordinates: 735650-736219. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 10, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28915|protein.P28915]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybfC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002404,ECOCYC:EG11523,GeneID:947288`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:735650-736219:+; feature_type=gene
