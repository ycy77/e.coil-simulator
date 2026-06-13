---
entity_id: "gene.b1229"
entity_type: "gene"
name: "tpr"
source_database: "NCBI RefSeq"
source_id: "gene-b1229"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1229"
  - "tpr"
---

# tpr

`gene.b1229`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1229`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tpr (gene.b1229) is a gene entity. It encodes tpr (protein.P02338). Encoded protein function: Protamine-like protein EcoCyc product frame: EG11016-MONOMER. Genomic coordinates: 1287087-1287176. EcoCyc protein note: Tpr is a basic protein with similarity to protamines . were unable to detect expression of SPA-tagged Tpr. The essentiality of tpr is unclear; mutants in the Keio collection appear to contain a partial duplication . Tpr: "tRNA followed by protamine-like protein"

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02338|protein.P02338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=tpr; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=tpr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004131,ECOCYC:EG11016,GeneID:946224`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1287087-1287176:-; feature_type=gene
