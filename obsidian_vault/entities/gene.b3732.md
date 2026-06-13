---
entity_id: "gene.b3732"
entity_type: "gene"
name: "atpD"
source_database: "NCBI RefSeq"
source_id: "gene-b3732"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3732"
  - "atpD"
---

# atpD

`gene.b3732`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3732`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpD (gene.b3732) is a gene entity. It encodes atpD (protein.P0ABB4). Encoded protein function: FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The catalytic sites are hosted primarily by the beta subunits. EcoCyc product frame: ATPD-MONOMER. EcoCyc synonyms: papB, uncD. Genomic coordinates: 3915993-3917375.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABB4|protein.P0ABB4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012208,ECOCYC:EG10101,GeneID:948244`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3915993-3917375:-; feature_type=gene
