---
entity_id: "gene.b4301"
entity_type: "gene"
name: "sgcE"
source_database: "NCBI RefSeq"
source_id: "gene-b4301"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4301"
  - "sgcE"
---

# sgcE

`gene.b4301`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4301`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgcE (gene.b4301) is a gene entity. It encodes sgcE (protein.P39362). Encoded protein function: FUNCTION: Probable pentose-5-phosphate 3-epimerase. {ECO:0000250|UniProtKB:P0AG07}. EcoCyc product frame: G7914-MONOMER. EcoCyc synonyms: yjhK. Genomic coordinates: 4526905-4527537. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 9, 2017.

## Biological Role

Repressed by slyA (protein.P0A8W2). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39362|protein.P39362]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgcE; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=sgcE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014097,ECOCYC:G7914,GeneID:948829`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4526905-4527537:-; feature_type=gene
