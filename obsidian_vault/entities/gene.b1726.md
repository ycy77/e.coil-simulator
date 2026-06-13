---
entity_id: "gene.b1726"
entity_type: "gene"
name: "yniB"
source_database: "NCBI RefSeq"
source_id: "gene-b1726"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1726"
  - "yniB"
---

# yniB

`gene.b1726`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1726`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yniB (gene.b1726) is a gene entity. It encodes yniB (protein.P76208). Encoded protein function: Uncharacterized protein YniB EcoCyc product frame: G6931-MONOMER. Genomic coordinates: 1808697-1809233. EcoCyc protein note: No information about this protein was found by a literature search conducted on January 19, 2007.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76208|protein.P76208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yniB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005757,ECOCYC:G6931,GeneID:945140`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1808697-1809233:-; feature_type=gene
