---
entity_id: "gene.b0386"
entity_type: "gene"
name: "proC"
source_database: "NCBI RefSeq"
source_id: "gene-b0386"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0386"
  - "proC"
---

# proC

`gene.b0386`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0386`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proC (gene.b0386) is a gene entity. It encodes proC (protein.P0A9L8). Encoded protein function: FUNCTION: Catalyzes the reduction of 1-pyrroline-5-carboxylate (PCA) to L-proline. Does not catalyze the reverse reaction. {ECO:0000255|HAMAP-Rule:MF_01925, ECO:0000269|PubMed:12133, ECO:0000269|PubMed:6296787}. EcoCyc product frame: PYRROLINECARBREDUCT-MONOMER. EcoCyc synonyms: pro(3), Pro2, pro3. Genomic coordinates: 404835-405644.

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9L8|protein.P0A9L8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001338,ECOCYC:EG10769,GeneID:945034`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:404835-405644:-; feature_type=gene
