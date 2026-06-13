---
entity_id: "gene.b2320"
entity_type: "gene"
name: "pdxB"
source_database: "NCBI RefSeq"
source_id: "gene-b2320"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2320"
  - "pdxB"
---

# pdxB

`gene.b2320`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2320`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdxB (gene.b2320) is a gene entity. It encodes pdxB (protein.P05459). Encoded protein function: FUNCTION: Catalyzes the oxidation of erythronate-4-phosphate to 3-hydroxy-2-oxo-4-phosphonooxybutanoate. {ECO:0000255|HAMAP-Rule:MF_01825}. EcoCyc product frame: ERYTHRON4PDEHYDROG-MONOMER. EcoCyc synonyms: usg-2. Genomic coordinates: 2436715-2437851.

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05459|protein.P05459]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007663,ECOCYC:G0-9461,GeneID:946785`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2436715-2437851:-; feature_type=gene
