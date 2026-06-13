---
entity_id: "gene.b3433"
entity_type: "gene"
name: "asd"
source_database: "NCBI RefSeq"
source_id: "gene-b3433"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3433"
  - "asd"
---

# asd

`gene.b3433`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3433`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asd (gene.b3433) is a gene entity. It encodes asd (protein.P0A9Q9). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent formation of L-aspartate-semialdehyde (L-ASA) by the reductive dephosphorylation of L-aspartyl-4-phosphate. {ECO:0000269|PubMed:11368768, ECO:0000269|PubMed:6102909}. EcoCyc product frame: ASP-SEMIALDEHYDE-DEHYDROGENASE-MONOMER. EcoCyc synonyms: dap, hom. Genomic coordinates: 3573775-3574878.

## Biological Role

Activated by argP (protein.P0A8S1).

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

- `encodes` --> [[protein.P0A9Q9|protein.P0A9Q9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=asd; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011211,ECOCYC:EG10088,GeneID:947939`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3573775-3574878:-; feature_type=gene
