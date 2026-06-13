---
entity_id: "gene.b3789"
entity_type: "gene"
name: "rffH"
source_database: "NCBI RefSeq"
source_id: "gene-b3789"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3789"
  - "rffH"
---

# rffH

`gene.b3789`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3789`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rffH (gene.b3789) is a gene entity. It encodes rffH (protein.P61887). Encoded protein function: FUNCTION: Catalyzes the formation of dTDP-glucose, from dTTP and glucose 1-phosphate, as well as its pyrophosphorolysis. {ECO:0000269|PubMed:7559340}. EcoCyc product frame: DTDPGLUCOSEPP2-MONOMER. EcoCyc synonyms: yifG. Genomic coordinates: 3973608-3974489.

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

- `encodes` --> [[protein.P61887|protein.P61887]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012379,ECOCYC:EG11454,GeneID:948299`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3973608-3974489:+; feature_type=gene
