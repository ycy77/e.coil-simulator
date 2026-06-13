---
entity_id: "gene.b2803"
entity_type: "gene"
name: "fucK"
source_database: "NCBI RefSeq"
source_id: "gene-b2803"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2803"
  - "fucK"
---

# fucK

`gene.b2803`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2803`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fucK (gene.b2803) is a gene entity. It encodes fucK (protein.P11553). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of L-fuculose. Can also phosphorylate, with lower efficiency, D-ribulose, D-xylulose and D-fructose. {ECO:0000255|HAMAP-Rule:MF_00986, ECO:0000269|PubMed:13905785}. EcoCyc product frame: FUCULOKIN-MONOMER. Genomic coordinates: 2937468-2938886. EcoCyc protein note: FucK can function as both an L-fuculokinase and a D-ribulokinase, the second enzyme of the L-fucose and D-arabinose degradation pathways, respectively. However, production of FucK is only induced by L-fucose . An fucK deletion mutant colonizes the mouse intestine as well as wild type, but is defective in maintenance of the population .

## Biological Role

Activated by crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11553|protein.P11553]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=fucK; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=fucK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009191,ECOCYC:EG10350,GeneID:946022`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2937468-2938886:+; feature_type=gene
