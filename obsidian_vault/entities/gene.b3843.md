---
entity_id: "gene.b3843"
entity_type: "gene"
name: "ubiD"
source_database: "NCBI RefSeq"
source_id: "gene-b3843"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3843"
  - "ubiD"
---

# ubiD

`gene.b3843`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3843`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiD (gene.b3843) is a gene entity. It encodes ubiD (protein.P0AAB4). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of 3-octaprenyl-4-hydroxy benzoate to 2-octaprenylphenol, an intermediate step in ubiquinone biosynthesis. {ECO:0000255|HAMAP-Rule:MF_01636, ECO:0000269|PubMed:782527}. EcoCyc product frame: EG11396-MONOMER. EcoCyc synonyms: yigY, yigC. Genomic coordinates: 4024988-4026481.

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAB4|protein.P0AAB4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012557,ECOCYC:EG11396,GeneID:948326`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4024988-4026481:+; feature_type=gene
