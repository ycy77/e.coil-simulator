---
entity_id: "gene.b0827"
entity_type: "gene"
name: "moeA"
source_database: "NCBI RefSeq"
source_id: "gene-b0827"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0827"
  - "moeA"
---

# moeA

`gene.b0827`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0827`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

moeA (gene.b0827) is a gene entity. It encodes moeA (protein.P12281). Encoded protein function: FUNCTION: Catalyzes the insertion of molybdate into adenylated molybdopterin with the concomitant release of AMP. {ECO:0000269|PubMed:15632135}. EcoCyc product frame: EG10153-MONOMER. EcoCyc synonyms: bisB, chlE, narE. Genomic coordinates: 865129-866364.

## Biological Role

Repressed by fnr (protein.P0A9E5). Activated by arcA (protein.P0A9Q1), nac (protein.Q47005).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12281|protein.P12281]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=moeA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=moeA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=moeA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002823,ECOCYC:EG10153,GeneID:945454`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:865129-866364:-; feature_type=gene
