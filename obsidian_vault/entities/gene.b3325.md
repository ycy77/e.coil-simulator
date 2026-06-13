---
entity_id: "gene.b3325"
entity_type: "gene"
name: "gspD"
source_database: "NCBI RefSeq"
source_id: "gene-b3325"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3325"
  - "gspD"
---

# gspD

`gene.b3325`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3325`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspD (gene.b3325) is a gene entity. It encodes gspD (protein.P45758). Encoded protein function: FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. This subunit would form the outer membrane channel. {ECO:0000250|UniProtKB:E3PJ86}. EcoCyc product frame: G7703-MONOMER. EcoCyc synonyms: yheF. Genomic coordinates: 3456377-3458329. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspD encodes the outer membrane channel or 'secretin' of gram-negative type II secretion systems (see ). Purified GspD adopts a pentadecameric structure forming a cylindrical channel; the K-12 GspD protomer consists of five domains: 3 N domains (N1, N2, N3) which form the periplasmic chamber plus the secretin and S domain which form the pore structure in the OM . gspD in E...

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45758|protein.P45758]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspD; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspD; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspD; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010879,ECOCYC:G7703,GeneID:947822`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3456377-3458329:+; feature_type=gene
