---
entity_id: "gene.b3875"
entity_type: "gene"
name: "ompL"
source_database: "NCBI RefSeq"
source_id: "gene-b3875"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3875"
  - "ompL"
---

# ompL

`gene.b3875`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3875`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompL (gene.b3875) is a gene entity. It encodes ompL (protein.P76773). Encoded protein function: FUNCTION: Outer membrane channel protein that allows an efficient diffusion of low-molecular-weight solutes such as small sugars and tetraglycine. However, the specific substrate recognized by the OmpL channel is unknown. {ECO:0000269|PubMed:12660153}. EcoCyc product frame: G7814-MONOMER. EcoCyc synonyms: yshA. Genomic coordinates: 4063603-4064295. EcoCyc protein note: OmpL is a member of the OmpG porin Family. OmpL localizes to the outer membrane and exhibits porin type properties allowing a non-specific group of solutes smaller than 600 Daltons to pass into and out of the periplasm . Sequence analysis suggests that it has a β-barrel structure consisting of 12 β-strands. . It has also been claimed to have an effect on redox potential in the periplasm , however this point is currently contested . OmpL has sequence similarity to members of the Cyclodextrin Porin (CDP) family . ompL exhibits mosaic evolution patterns in E. coli .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76773|protein.P76773]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012659,ECOCYC:G7814,GeneID:948366`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4063603-4064295:-; feature_type=gene
