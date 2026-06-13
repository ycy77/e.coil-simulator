---
entity_id: "gene.b1948"
entity_type: "gene"
name: "fliP"
source_database: "NCBI RefSeq"
source_id: "gene-b1948"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1948"
  - "fliP"
---

# fliP

`gene.b1948`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1948`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliP (gene.b1948) is a gene entity. It encodes fliP (protein.P0AC05). Encoded protein function: FUNCTION: Plays a role in the flagellum-specific transport system. EcoCyc product frame: EG11975-MONOMER. EcoCyc synonyms: flaR. Genomic coordinates: 2021869-2022606. EcoCyc protein note: FliP is one of six integral membrane components of the flagellar export apparatus . FliP has a substantial periplasmic domain between two of its four transmembrane domains .

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC05|protein.P0AC05]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006475,ECOCYC:EG11975,GeneID:946462`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2021869-2022606:+; feature_type=gene
