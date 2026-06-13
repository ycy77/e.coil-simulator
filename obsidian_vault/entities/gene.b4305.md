---
entity_id: "gene.b4305"
entity_type: "gene"
name: "sgcX"
source_database: "NCBI RefSeq"
source_id: "gene-b4305"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4305"
  - "sgcX"
---

# sgcX

`gene.b4305`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4305`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgcX (gene.b4305) is a gene entity. It encodes sgcX (protein.P39366). Encoded protein function: Putative aminopeptidase SgcX (EC 3.4.11.-) EcoCyc product frame: SGCB-MONOMER. EcoCyc synonyms: yjhO. Genomic coordinates: 4530530-4531651. EcoCyc protein note: An sgcX deletion mutant is more sensitive to kasugamycin than wild type .

## Biological Role

Repressed by slyA (protein.P0A8W2). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39366|protein.P39366]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgcX; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=sgcX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014112,ECOCYC:EG12557,GeneID:948840`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4530530-4531651:-; feature_type=gene
