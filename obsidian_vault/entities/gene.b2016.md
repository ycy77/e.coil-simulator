---
entity_id: "gene.b2016"
entity_type: "gene"
name: "yeeZ"
source_database: "NCBI RefSeq"
source_id: "gene-b2016"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2016"
  - "yeeZ"
---

# yeeZ

`gene.b2016`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2016`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeeZ (gene.b2016) is a gene entity. It encodes yeeZ (protein.P0AD12). Encoded protein function: Protein YeeZ EcoCyc product frame: G7089-MONOMER. Genomic coordinates: 2088304-2089128. EcoCyc protein note: In a study of the E. coli complexome, YeeZ was found in a cytoplasmic complex together with YbbN and YeeN .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD12|protein.P0AD12]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yeeZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006702,ECOCYC:G7089,GeneID:946538`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2088304-2089128:-; feature_type=gene
