---
entity_id: "gene.b0558"
entity_type: "gene"
name: "ybcV"
source_database: "NCBI RefSeq"
source_id: "gene-b0558"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0558"
  - "ybcV"
---

# ybcV

`gene.b0558`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0558`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybcV (gene.b0558) is a gene entity. It encodes ybcV (protein.P77598). Encoded protein function: Uncharacterized protein YbcV EcoCyc product frame: G6313-MONOMER. Genomic coordinates: 579184-579594. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 20, 2018.

## Biological Role

Repressed by nac (protein.Q47005). Activated by pdhR (protein.P0ACL9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77598|protein.P77598]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ybcV; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybcV; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001907,ECOCYC:G6313,GeneID:945178`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:579184-579594:-; feature_type=gene
