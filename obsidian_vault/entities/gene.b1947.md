---
entity_id: "gene.b1947"
entity_type: "gene"
name: "fliO"
source_database: "NCBI RefSeq"
source_id: "gene-b1947"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1947"
  - "fliO"
---

# fliO

`gene.b1947`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1947`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliO (gene.b1947) is a gene entity. It encodes fliO (protein.P22586). Encoded protein function: Flagellar protein FliO EcoCyc product frame: EG11224-MONOMER. EcoCyc synonyms: flbD. Genomic coordinates: 2021504-2021869. EcoCyc protein note: FliO is one of six integral membrane components of the flagellar export apparatus . FliO has a small N-terminal cytoplasmic domain, a hydrophobic domain consisting of a single transmembrane helix and a considerable periplasmic domain .

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22586|protein.P22586]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006473,ECOCYC:EG11224,GeneID:946458`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2021504-2021869:+; feature_type=gene
