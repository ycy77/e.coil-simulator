---
entity_id: "gene.b0596"
entity_type: "gene"
name: "entA"
source_database: "NCBI RefSeq"
source_id: "gene-b0596"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0596"
  - "entA"
---

# entA

`gene.b0596`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0596`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entA (gene.b0596) is a gene entity. It encodes entA (protein.P15047). Encoded protein function: FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. Catalyzes the reversible NAD-dependent oxidation of the C3-hydroxyl group of 2,3-dihydro-2,3-dihydroxybenzoate (2,3-diDHB), producing the transient intermediate 2-hydroxy-3-oxo-4,6-cyclohexadiene-1-carboxylate, which undergoes rapid aromatization to the final product, 2,3-dihydroxybenzoate (2,3-DHB). Only the compounds with a C3-hydroxyl group such as methyl 2,3-dihydro-2,3-dihydroxybenzoate, methyl-3-hydroxy-1,4-cyclohexadiene-1-carboxylate, trans-3-hydroxy-2-cyclohexene-1-carboxylate, cis-3-hydroxy-4-cyclohexene-1-carboxylate, cis-3-hydroxycyclohexane-1-carboxylic acid are oxidized to the corresponding ketone products. The stereospecificity of the C3 allylic alcohol group oxidation is 3R in a 1R,3R dihydro substrate. It can also increase the DHB-AMP ligase activity of EntE by interaction EntE. {ECO:0000269|PubMed:21166461, ECO:0000269|PubMed:2144454, ECO:0000269|PubMed:2521622}. EcoCyc product frame: ENTA-MONOMER. Genomic coordinates: 628551-629297.

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15047|protein.P15047]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=entA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002054,ECOCYC:EG10259,GeneID:945284`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:628551-629297:+; feature_type=gene
