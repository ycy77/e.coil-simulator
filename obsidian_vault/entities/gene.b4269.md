---
entity_id: "gene.b4269"
entity_type: "gene"
name: "ahr"
source_database: "NCBI RefSeq"
source_id: "gene-b4269"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4269"
  - "ahr"
---

# ahr

`gene.b4269`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4269`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ahr (gene.b4269) is a gene entity. It encodes ahr (protein.P27250). Encoded protein function: FUNCTION: Catalyzes the reduction of a wide range of aldehydes including aliphatic fatty aldehydes (C4-C16), into their corresponding alcohols. Has a strong preference for NADPH over NADH as the electron donor. Cannot use glyceraldehyde or a ketone as substrate. Is a relevant source of NADPH-dependent aldehyde reductase activity in E.coli. The in vivo functions of Ahr has yet to be determined. {ECO:0000269|PubMed:22731523, ECO:0000269|PubMed:23093176, ECO:0000269|PubMed:23248280}. EcoCyc product frame: EG11436-MONOMER. EcoCyc synonyms: yjgB. Genomic coordinates: 4495190-4496209.

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27250|protein.P27250]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013982,ECOCYC:EG11436,GeneID:948802`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4495190-4496209:-; feature_type=gene
