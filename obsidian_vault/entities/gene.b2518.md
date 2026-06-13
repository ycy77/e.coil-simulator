---
entity_id: "gene.b2518"
entity_type: "gene"
name: "ndk"
source_database: "NCBI RefSeq"
source_id: "gene-b2518"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2518"
  - "ndk"
---

# ndk

`gene.b2518`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2518`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ndk (gene.b2518) is a gene entity. It encodes ndk (protein.P0A763). Encoded protein function: FUNCTION: Major role in the synthesis of nucleoside triphosphates other than ATP. The ATP gamma phosphate is transferred to the NDP beta phosphate via a ping-pong mechanism, using a phosphorylated active-site intermediate. {ECO:0000255|HAMAP-Rule:MF_00451, ECO:0000269|PubMed:7730286}. EcoCyc product frame: NUCLEOSIDE-DIP-KIN-MONOMER. Genomic coordinates: 2644433-2644864.

## Biological Role

Repressed by arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A763|protein.P0A763]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=ndk; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008291,ECOCYC:EG10650,GeneID:945611`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2644433-2644864:-; feature_type=gene
