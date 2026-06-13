---
entity_id: "gene.b0323"
entity_type: "gene"
name: "yahI"
source_database: "NCBI RefSeq"
source_id: "gene-b0323"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0323"
  - "yahI"
---

# yahI

`gene.b0323`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0323`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yahI (gene.b0323) is a gene entity. It encodes yahI (protein.P77624). Encoded protein function: Carbamate kinase-like protein YahI EcoCyc product frame: G6188-MONOMER. Genomic coordinates: 340165-341115. EcoCyc protein note: In an in silico screen, yahI was predicted to improve isoprenoid precursor supply and thereby heterologous lycopene biosynthesis when mutated. The prediction was tested, and a yahI mutation increases lycopene yield .

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77624|protein.P77624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001107,ECOCYC:G6188,GeneID:944984`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:340165-341115:+; feature_type=gene
