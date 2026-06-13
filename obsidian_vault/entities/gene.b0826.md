---
entity_id: "gene.b0826"
entity_type: "gene"
name: "moeB"
source_database: "NCBI RefSeq"
source_id: "gene-b0826"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0826"
  - "moeB"
---

# moeB

`gene.b0826`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0826`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

moeB (gene.b0826) is a gene entity. It encodes moeB (protein.P12282). Encoded protein function: FUNCTION: Catalyzes the adenylation by ATP of the carboxyl group of the C-terminal glycine of sulfur carrier protein MoaD. {ECO:0000269|PubMed:11290749, ECO:0000269|PubMed:11463785}. EcoCyc product frame: EG10154-MONOMER. EcoCyc synonyms: chlN. Genomic coordinates: 864380-865129.

## Biological Role

Repressed by fnr (protein.P0A9E5). Activated by arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12282|protein.P12282]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=moeB; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=moeB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002820,ECOCYC:EG10154,GeneID:945452`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:864380-865129:-; feature_type=gene
