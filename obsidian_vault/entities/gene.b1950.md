---
entity_id: "gene.b1950"
entity_type: "gene"
name: "fliR"
source_database: "NCBI RefSeq"
source_id: "gene-b1950"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1950"
  - "fliR"
---

# fliR

`gene.b1950`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1950`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliR (gene.b1950) is a gene entity. It encodes fliR (protein.P33135). Encoded protein function: FUNCTION: Role in flagellar biosynthesis. EcoCyc product frame: EG11977-MONOMER. EcoCyc synonyms: flaP. Genomic coordinates: 2022893-2023678. EcoCyc protein note: FliR is one of six integral membrane components of the flagellar export apparatus . FliR has five or six transmembrane helices connected by short loops .

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33135|protein.P33135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006479,ECOCYC:EG11977,GeneID:946464`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2022893-2023678:+; feature_type=gene
