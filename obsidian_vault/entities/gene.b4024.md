---
entity_id: "gene.b4024"
entity_type: "gene"
name: "lysC"
source_database: "NCBI RefSeq"
source_id: "gene-b4024"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4024"
  - "lysC"
---

# lysC

`gene.b4024`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4024`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysC (gene.b4024) is a gene entity. It encodes lysC (protein.P08660). Encoded protein function: Lysine-sensitive aspartokinase 3 (EC 2.7.2.4) (Aspartate kinase III) (AKIII) (Lysine-sensitive aspartokinase III) EcoCyc product frame: ASPKINIII-MONOMER. EcoCyc synonyms: apk. Genomic coordinates: 4231884-4233233.

## Biological Role

Activated by rpoD (protein.P00579), argP (protein.P0A8S1).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08660|protein.P08660]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lysC; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=lysC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013156,ECOCYC:EG10550,GeneID:948531`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4231884-4233233:-; feature_type=gene
