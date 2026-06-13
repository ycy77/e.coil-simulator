---
entity_id: "gene.b0440"
entity_type: "gene"
name: "hupB"
source_database: "NCBI RefSeq"
source_id: "gene-b0440"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0440"
  - "hupB"
---

# hupB

`gene.b0440`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0440`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hupB (gene.b0440) is a gene entity. It encodes hupB (protein.P0ACF4). Encoded protein function: FUNCTION: Histone-like DNA-binding protein which is capable of wrapping DNA to stabilize it, and thus to prevent its denaturation under extreme environmental conditions. {ECO:0000305|PubMed:24916461}. EcoCyc product frame: EG10467-MONOMER. EcoCyc synonyms: dpeA, dbhB, hopD. Genomic coordinates: 461451-461723.

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACF4|protein.P0ACF4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hupB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hupB; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=hupB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001527,ECOCYC:EG10467,GeneID:949095`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:461451-461723:+; feature_type=gene
