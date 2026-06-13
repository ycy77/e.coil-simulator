---
entity_id: "gene.b3488"
entity_type: "gene"
name: "yhiJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3488"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3488"
  - "yhiJ"
---

# yhiJ

`gene.b3488`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3488`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhiJ (gene.b3488) is a gene entity. It encodes yhiJ (protein.P37627). Encoded protein function: Uncharacterized protein YhiJ EcoCyc product frame: EG12225-MONOMER. Genomic coordinates: 3630968-3632590. EcoCyc protein note: Gap filling of the E. coli iJO1366 model suggested that YhiJ is a putative myo-inositol oxygenase. While a wild-type strain can grow very slowly on myo-inositol as the sole source of carbon, a ΔyhiJ mutant is unable to do so .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37627|protein.P37627]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhiJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011387,ECOCYC:EG12225,GeneID:948001`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3630968-3632590:-; feature_type=gene
