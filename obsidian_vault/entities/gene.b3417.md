---
entity_id: "gene.b3417"
entity_type: "gene"
name: "malP"
source_database: "NCBI RefSeq"
source_id: "gene-b3417"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3417"
  - "malP"
---

# malP

`gene.b3417`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3417`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malP (gene.b3417) is a gene entity. It encodes malP (protein.P00490). Encoded protein function: FUNCTION: Phosphorylase is an important allosteric enzyme in carbohydrate metabolism. Enzymes from different sources differ in their regulatory mechanisms and in their natural substrates. However, all known phosphorylases share catalytic and structural properties. EcoCyc product frame: MALDEXPHOSPHORYL-MONOMER. EcoCyc synonyms: malA, blu. Genomic coordinates: 3550080-3552473.

## Biological Role

Activated by malT (protein.P06993).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00490|protein.P00490]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011154,ECOCYC:EG10560,GeneID:947922`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3550080-3552473:-; feature_type=gene
