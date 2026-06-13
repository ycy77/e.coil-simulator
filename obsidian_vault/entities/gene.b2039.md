---
entity_id: "gene.b2039"
entity_type: "gene"
name: "rfbA"
source_database: "NCBI RefSeq"
source_id: "gene-b2039"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2039"
  - "rfbA"
---

# rfbA

`gene.b2039`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2039`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rfbA (gene.b2039) is a gene entity. It encodes rfbA (protein.P37744). Encoded protein function: FUNCTION: Catalyzes the formation of dTDP-glucose, from dTTP and glucose 1-phosphate, as well as its pyrophosphorolysis. {ECO:0000269|PubMed:11697907}. EcoCyc product frame: DTDPGLUCOSEPP-MONOMER. EcoCyc synonyms: rmlA, som. Genomic coordinates: 2110138-2111019.

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37744|protein.P37744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006762,ECOCYC:EG11978,GeneID:945154`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2110138-2111019:-; feature_type=gene
