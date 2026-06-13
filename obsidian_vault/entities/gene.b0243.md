---
entity_id: "gene.b0243"
entity_type: "gene"
name: "proA"
source_database: "NCBI RefSeq"
source_id: "gene-b0243"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0243"
  - "proA"
---

# proA

`gene.b0243`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0243`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proA (gene.b0243) is a gene entity. It encodes proA (protein.P07004). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of L-glutamate 5-phosphate into L-glutamate 5-semialdehyde and phosphate. The product spontaneously undergoes cyclization to form 1-pyrroline-5-carboxylate. {ECO:0000255|HAMAP-Rule:MF_00412, ECO:0000269|PubMed:7034716, ECO:0000269|PubMed:7035170}. EcoCyc product frame: GLUTSEMIALDEHYDROG-MONOMER. EcoCyc synonyms: pro(1), pro1. Genomic coordinates: 261503-262756.

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07004|protein.P07004]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000832,ECOCYC:EG10767,GeneID:946680`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:261503-262756:+; feature_type=gene
