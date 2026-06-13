---
entity_id: "gene.b0004"
entity_type: "gene"
name: "thrC"
source_database: "NCBI RefSeq"
source_id: "gene-b0004"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0004"
  - "thrC"
---

# thrC

`gene.b0004`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0004`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrC (gene.b0004) is a gene entity. It encodes thrC (protein.P00934). Encoded protein function: FUNCTION: Catalyzes the gamma-elimination of phosphate from L-phosphohomoserine and the beta-addition of water to produce L-threonine. To a lesser extent, is able to slowly catalyze the deamination of L-threonine into alpha-ketobutyrate and that of L-serine and 3-chloroalanine into pyruvate. Is also able to rapidly convert vinylglycine to threonine, which proves that the pyridoxal p-quinonoid of vinylglycine is an intermediate in the TS reaction. {ECO:0000269|PubMed:7907888}. EcoCyc product frame: THRESYN-MONOMER. Genomic coordinates: 3734-5020. EcoCyc protein note: Threonine synthase (ThrC) carries out the final step in the biosynthesis of L-threonine, the dephosphorylation of O-phospho-homoserine . A reaction mechanism based on extensive evaluation of the enzymatic activity with alternative substrates and inhibitors has been proposed .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00934|protein.P00934]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=thrC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000012,ECOCYC:EG11000,GeneID:945198`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3734-5020:+; feature_type=gene
