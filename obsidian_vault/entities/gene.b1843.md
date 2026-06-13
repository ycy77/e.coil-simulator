---
entity_id: "gene.b1843"
entity_type: "gene"
name: "yobB"
source_database: "NCBI RefSeq"
source_id: "gene-b1843"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1843"
  - "yobB"
---

# yobB

`gene.b1843`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1843`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yobB (gene.b1843) is a gene entity. It encodes yobB (protein.P76280). Encoded protein function: Uncharacterized protein YobB EcoCyc product frame: G7015-MONOMER. Genomic coordinates: 1925440-1926096. EcoCyc protein note: No information about this protein was found by a literature search conducted on December 18, 2019.

## Biological Role

Repressed by ompR (protein.P0AA16), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76280|protein.P76280]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=yobB; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yobB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006129,ECOCYC:G7015,GeneID:948329`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1925440-1926096:+; feature_type=gene
