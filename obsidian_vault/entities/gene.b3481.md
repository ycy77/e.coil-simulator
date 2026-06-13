---
entity_id: "gene.b3481"
entity_type: "gene"
name: "nikR"
source_database: "NCBI RefSeq"
source_id: "gene-b3481"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3481"
  - "nikR"
---

# nikR

`gene.b3481`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3481`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nikR (gene.b3481) is a gene entity. It encodes nikR (protein.P0A6Z6). Encoded protein function: FUNCTION: Transcriptional repressor of the nikABCDE operon. Is active in the presence of excessive concentrations of intracellular nickel. EcoCyc product frame: EG11519-MONOMER. EcoCyc synonyms: yhhG. Genomic coordinates: 3618588-3618989.

## Biological Role

Repressed by nikR (protein.P0A6Z6). Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Z6|protein.P0A6Z6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nikR; function=+
- `represses` <-- [[protein.P0A6Z6|protein.P0A6Z6]] `RegulonDB` `S` - regulator=NikR; target=nikR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011366,ECOCYC:EG11519,GeneID:947995`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3618588-3618989:+; feature_type=gene
