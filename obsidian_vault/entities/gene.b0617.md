---
entity_id: "gene.b0617"
entity_type: "gene"
name: "citD"
source_database: "NCBI RefSeq"
source_id: "gene-b0617"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0617"
  - "citD"
---

# citD

`gene.b0617`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0617`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citD (gene.b0617) is a gene entity. It encodes citD (protein.P69330). Encoded protein function: FUNCTION: Covalent carrier of the coenzyme of citrate lyase. EcoCyc product frame: ACPSUB-MONOMER. EcoCyc synonyms: ybdX. Genomic coordinates: 650487-650783.

## Biological Role

Activated by dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69330|protein.P69330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=citD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002124,ECOCYC:G6343,GeneID:945415`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:650487-650783:-; feature_type=gene
