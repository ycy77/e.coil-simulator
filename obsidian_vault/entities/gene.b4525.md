---
entity_id: "gene.b4525"
entity_type: "gene"
name: "ymjC"
source_database: "NCBI RefSeq"
source_id: "gene-b4525"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4525"
  - "ymjC"
---

# ymjC

`gene.b4525`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4525`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymjC (gene.b4525) is a gene entity. It encodes ymjC (protein.Q2EER5). Encoded protein function: Protein YmjC EcoCyc product frame: MONOMER0-2668. Genomic coordinates: 1390680-1390862. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 12, 2018.

## Biological Role

Repressed by pgrR (protein.P77333).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q2EER5|protein.Q2EER5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=ymjC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285046,ECOCYC:G0-10446,GeneID:1450258`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1390680-1390862:-; feature_type=gene
