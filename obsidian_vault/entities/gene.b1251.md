---
entity_id: "gene.b1251"
entity_type: "gene"
name: "yciI"
source_database: "NCBI RefSeq"
source_id: "gene-b1251"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1251"
  - "yciI"
---

# yciI

`gene.b1251`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1251`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciI (gene.b1251) is a gene entity. It encodes yciI (protein.P0AB55). Encoded protein function: Protein YciI EcoCyc product frame: EG11607-MONOMER. Genomic coordinates: 1310569-1310865. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 16, 2017.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB55|protein.P0AB55]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=yciI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004192,ECOCYC:EG11607,GeneID:949085`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1310569-1310865:-; feature_type=gene
