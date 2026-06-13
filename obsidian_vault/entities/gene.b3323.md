---
entity_id: "gene.b3323"
entity_type: "gene"
name: "gspA"
source_database: "NCBI RefSeq"
source_id: "gene-b3323"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3323"
  - "gspA"
---

# gspA

`gene.b3323`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3323`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspA (gene.b3323) is a gene entity. It encodes gspA (protein.P45756). Encoded protein function: FUNCTION: May play a regulatory role under conditions of derepressed gsp gene expression. {ECO:0000269|PubMed:11118204}. EcoCyc product frame: G7701-MONOMER. EcoCyc synonyms: yheD. Genomic coordinates: 3453929-3455398. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system (T2SS); the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . GspA is predicted to be a bitopic inner membrane protein . The inner membrane proteins GspA and GspB contribute to G7703-MONOMER secretin assembly and transport in some gram-negative T2SSs (see ). gsp: general secretory pathway (and see )

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45756|protein.P45756]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspA; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=gspA; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010867,ECOCYC:G7701,GeneID:947825`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3453929-3455398:-; feature_type=gene
