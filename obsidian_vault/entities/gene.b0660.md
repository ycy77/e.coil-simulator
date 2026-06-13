---
entity_id: "gene.b0660"
entity_type: "gene"
name: "ybeZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0660"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0660"
  - "ybeZ"
---

# ybeZ

`gene.b0660`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0660`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeZ (gene.b0660) is a gene entity. It encodes ybeZ (protein.P0A9K3). Encoded protein function: PhoH-like protein EcoCyc product frame: G6363-MONOMER. EcoCyc synonyms: phoL. Genomic coordinates: 692338-693378. EcoCyc protein note: YbeZ belongs to the Bacillus subtilis subfamily of PhoH proteins . YbeZ interacts with G6362-MONOMER YbeY .

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9K3|protein.P0A9K3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ybeZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002257,ECOCYC:G6363,GeneID:948044`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:692338-693378:-; feature_type=gene
