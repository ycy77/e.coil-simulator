---
entity_id: "gene.b3399"
entity_type: "gene"
name: "yrfG"
source_database: "NCBI RefSeq"
source_id: "gene-b3399"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3399"
  - "yrfG"
---

# yrfG

`gene.b3399`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3399`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yrfG (gene.b3399) is a gene entity. It encodes yrfG (protein.P64636). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of different purine nucleotides (GMP and IMP). Also hydrolyzes flavin mononucleotide (FMN). {ECO:0000269|PubMed:16990279}. EcoCyc product frame: G7742-MONOMER. Genomic coordinates: 3528669-3529337. EcoCyc protein note: YrfG is a purine nucleotidase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. It shows a low level of discrimination between its preferred substrates .

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64636|protein.P64636]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011092,ECOCYC:G7742,GeneID:947904`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3528669-3529337:+; feature_type=gene
