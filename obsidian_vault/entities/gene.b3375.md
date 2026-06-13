---
entity_id: "gene.b3375"
entity_type: "gene"
name: "frlR"
source_database: "NCBI RefSeq"
source_id: "gene-b3375"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3375"
  - "frlR"
---

# frlR

`gene.b3375`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3375`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frlR (gene.b3375) is a gene entity. It encodes frlR (protein.P45544). Encoded protein function: FUNCTION: May regulate the transcription of the frlABCDR operon, involved in the utilization of fructoselysine and psicoselysine. {ECO:0000305|PubMed:12147680}. EcoCyc product frame: G7727-MONOMER. EcoCyc synonyms: yhfR. Genomic coordinates: 3504052-3504783.

## Biological Role

Repressed by frlR (protein.P45544). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45544|protein.P45544]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=frlR; function=+
- `represses` <-- [[protein.P45544|protein.P45544]] `RegulonDB` `C` - regulator=FrlR; target=frlR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011031,ECOCYC:G7727,GeneID:947885`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3504052-3504783:+; feature_type=gene
