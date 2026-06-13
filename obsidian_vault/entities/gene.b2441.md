---
entity_id: "gene.b2441"
entity_type: "gene"
name: "eutB"
source_database: "NCBI RefSeq"
source_id: "gene-b2441"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2441"
  - "eutB"
---

# eutB

`gene.b2441`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2441`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutB (gene.b2441) is a gene entity. It encodes eutB (protein.P0AEJ6). Encoded protein function: FUNCTION: Catalyzes the deamination of various vicinal amino-alcohols to oxo compounds (PubMed:19762342). Allows this organism to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12. It is spontaneously inactivated by its substrate and reactivated by EutA (PubMed:15466038). {ECO:0000269|PubMed:15466038, ECO:0000269|PubMed:19762342, ECO:0000305|PubMed:2197274}. EcoCyc product frame: EUTB-MONOMER. Genomic coordinates: 2557318-2558679.

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEJ6|protein.P0AEJ6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008046,ECOCYC:EG50006,GeneID:946924`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2557318-2558679:-; feature_type=gene
