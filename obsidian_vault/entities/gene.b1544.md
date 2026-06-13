---
entity_id: "gene.b1544"
entity_type: "gene"
name: "ydfK"
source_database: "NCBI RefSeq"
source_id: "gene-b1544"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1544"
  - "ydfK"
---

# ydfK

`gene.b1544`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1544`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfK (gene.b1544) is a gene entity. It encodes ydfK (protein.P76154). Encoded protein function: Cold shock protein YdfK EcoCyc product frame: G6818-MONOMER. Genomic coordinates: 1633072-1633305. EcoCyc protein note: The 5' UTR of ydfK is similar to that of ynaE . Expression of both genes is upregulated by cold shock .

## Biological Role

Repressed by nac (protein.Q47005). Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76154|protein.P76154]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ydfK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydfK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005161,ECOCYC:G6818,GeneID:947451`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1633072-1633305:+; feature_type=gene
