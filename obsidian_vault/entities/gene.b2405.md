---
entity_id: "gene.b2405"
entity_type: "gene"
name: "xapR"
source_database: "NCBI RefSeq"
source_id: "gene-b2405"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2405"
  - "xapR"
---

# xapR

`gene.b2405`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2405`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xapR (gene.b2405) is a gene entity. It encodes xapR (protein.P23841). Encoded protein function: FUNCTION: Positive regulator required for the expression of xapA and xapB. Binds to the inducer xanthosine. EcoCyc product frame: EG11146-MONOMER. EcoCyc synonyms: pRndR, pndR, yfeB. Genomic coordinates: 2521593-2522477.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23841|protein.P23841]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=xapR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007922,ECOCYC:EG11146,GeneID:946862`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2521593-2522477:-; feature_type=gene
