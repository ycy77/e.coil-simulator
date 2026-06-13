---
entity_id: "gene.b0616"
entity_type: "gene"
name: "citE"
source_database: "NCBI RefSeq"
source_id: "gene-b0616"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0616"
  - "citE"
---

# citE

`gene.b0616`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0616`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citE (gene.b0616) is a gene entity. It encodes citE (protein.P0A9I1). Encoded protein function: FUNCTION: Represents a citryl-ACP lyase. {ECO:0000250}. EcoCyc product frame: CITRYLY-MONOMER. EcoCyc synonyms: ybdW. Genomic coordinates: 649582-650490.

## Biological Role

Activated by dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9I1|protein.P0A9I1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=citE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002122,ECOCYC:G6342,GeneID:945406`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:649582-650490:-; feature_type=gene
