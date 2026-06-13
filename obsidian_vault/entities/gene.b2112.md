---
entity_id: "gene.b2112"
entity_type: "gene"
name: "yehE"
source_database: "NCBI RefSeq"
source_id: "gene-b2112"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2112"
  - "yehE"
---

# yehE

`gene.b2112`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2112`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehE (gene.b2112) is a gene entity. It encodes yehE (protein.P33344). Encoded protein function: Uncharacterized protein YehE EcoCyc product frame: EG11991-MONOMER. Genomic coordinates: 2192515-2192796. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 23, 2017.

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33344|protein.P33344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P37338|protein.P37338]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yehE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006984,ECOCYC:EG11991,GeneID:946615`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2192515-2192796:-; feature_type=gene
