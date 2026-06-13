---
entity_id: "gene.b0133"
entity_type: "gene"
name: "panC"
source_database: "NCBI RefSeq"
source_id: "gene-b0133"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0133"
  - "panC"
---

# panC

`gene.b0133`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0133`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

panC (gene.b0133) is a gene entity. It encodes panC (protein.P31663). Encoded protein function: FUNCTION: Catalyzes the condensation of pantoate with beta-alanine in an ATP-dependent reaction via a pantoyl-adenylate intermediate. {ECO:0000269|PubMed:357689}. EcoCyc product frame: PANTOATE-BETA-ALANINE-LIG-MONOMER. Genomic coordinates: 147944-148795. EcoCyc protein note: Pantothenate synthetase (PanC) catalyzes the ATP hydrolysis-dependent synthesis of pantothenate from β-alanine and pantoate . The enzyme from strains W or B requires both monovalent and divalent cations . The pantothenate:β-alanine exchange reaction depends on the presence of AMP, which supports the two-step Bi Uni Uni Bi reaction mechanism with pantoyl adenylate as the reaction intermediate . Crystal structures of the full length enzyme and its N-terminal domain have been solved. Pantothenate synthetase is dimeric both in solution and the crystal structure. It is a member of the cytidylyltransferase superfamily, with an N-terminal Rossmann fold domain containing the active site and a C-terminal domain that forms a hinged lid . The substrate pantoate is able to bind within the ATP-binding pocket of the N-terminal domain . Molecular dynamics simulations suggest that motions of the C-terminal domain dominate the functional dynamics of the E. coli enzyme . panC mutants are auxotrophic for pantothenate...

## Enriched Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31663|protein.P31663]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000465,ECOCYC:EG11746,GeneID:944958`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:147944-148795:-; feature_type=gene
