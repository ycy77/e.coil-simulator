---
entity_id: "gene.b2977"
entity_type: "gene"
name: "glcG"
source_database: "NCBI RefSeq"
source_id: "gene-b2977"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2977"
  - "glcG"
---

# glcG

`gene.b2977`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2977`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glcG (gene.b2977) is a gene entity. It encodes glcG (protein.P0AEQ1). Encoded protein function: Protein GlcG EcoCyc product frame: G7543-MONOMER. EcoCyc synonyms: yghC. Genomic coordinates: 3123827-3124231. EcoCyc protein note: GlcG is a protein of unknown function encoded by a gene within the glycolate utilization operon .

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by glcC (protein.P0ACL5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEQ1|protein.P0AEQ1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACL5|protein.P0ACL5]] `RegulonDB` `S` - regulator=GlcC; target=glcG; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=glcG; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=glcG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009769,ECOCYC:G7543,GeneID:947473`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3123827-3124231:-; feature_type=gene
