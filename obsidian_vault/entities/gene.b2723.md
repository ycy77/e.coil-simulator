---
entity_id: "gene.b2723"
entity_type: "gene"
name: "hycC"
source_database: "NCBI RefSeq"
source_id: "gene-b2723"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2723"
  - "hycC"
---

# hycC

`gene.b2723`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2723`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycC (gene.b2723) is a gene entity. It encodes hycC (protein.P16429). Encoded protein function: Formate hydrogenlyase subunit 3 (FHL subunit 3) (Hydrogenase-3 component C) EcoCyc product frame: HYCC-MONOMER. EcoCyc synonyms: hevC. Genomic coordinates: 2847415-2849241.

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16429|protein.P16429]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycC; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycC; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008948,ECOCYC:EG10476,GeneID:945327`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2847415-2849241:-; feature_type=gene
