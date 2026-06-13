---
entity_id: "gene.b3501"
entity_type: "gene"
name: "arsR"
source_database: "NCBI RefSeq"
source_id: "gene-b3501"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3501"
  - "arsR"
---

# arsR

`gene.b3501`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3501`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arsR (gene.b3501) is a gene entity. It encodes arsR (protein.P37309). Encoded protein function: FUNCTION: Transcriptional repressor for the arsEFG operon. ArsE is a trans-acting regulatory protein which controls its own expression. The repressive effect of ArsE is alleviated by oxyions of +III oxidation state of arsenic, antimony, and bismuth, as well as arsenate (As(V)) (By similarity). {ECO:0000250}. EcoCyc product frame: EG12235-MONOMER. EcoCyc synonyms: arsE. Genomic coordinates: 3648528-3648881.

## Biological Role

Repressed by arsR (protein.P37309). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37309|protein.P37309]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=arsR; function=+
- `represses` <-- [[protein.P37309|protein.P37309]] `RegulonDB` `S` - regulator=ArsR; target=arsR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011435,ECOCYC:EG12235,GeneID:948013`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3648528-3648881:+; feature_type=gene
