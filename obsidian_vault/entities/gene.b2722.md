---
entity_id: "gene.b2722"
entity_type: "gene"
name: "hycD"
source_database: "NCBI RefSeq"
source_id: "gene-b2722"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2722"
  - "hycD"
---

# hycD

`gene.b2722`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2722`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycD (gene.b2722) is a gene entity. It encodes hycD (protein.P16430). Encoded protein function: Formate hydrogenlyase subunit 4 (FHL subunit 4) (Hydrogenase 3 component D) EcoCyc product frame: HYCD-MONOMER. EcoCyc synonyms: hevD. Genomic coordinates: 2846489-2847412.

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16430|protein.P16430]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycD; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycD; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008946,ECOCYC:EG10477,GeneID:948994`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2846489-2847412:-; feature_type=gene
