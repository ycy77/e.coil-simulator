---
entity_id: "gene.b1949"
entity_type: "gene"
name: "fliQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1949"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1949"
  - "fliQ"
---

# fliQ

`gene.b1949`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1949`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliQ (gene.b1949) is a gene entity. It encodes fliQ (protein.P0AC07). Encoded protein function: FUNCTION: Required for the assembly of the rivet at the earliest stage of flagellar biosynthesis. EcoCyc product frame: EG11976-MONOMER. EcoCyc synonyms: flaQ. Genomic coordinates: 2022616-2022885. EcoCyc protein note: FliQ is one of six integral membrane components of the flagellar export apparatus . FliQ has two transmembrane domains .

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC07|protein.P0AC07]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006477,ECOCYC:EG11976,GeneID:946463`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2022616-2022885:+; feature_type=gene
