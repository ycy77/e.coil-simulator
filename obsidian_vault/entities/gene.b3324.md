---
entity_id: "gene.b3324"
entity_type: "gene"
name: "gspC"
source_database: "NCBI RefSeq"
source_id: "gene-b3324"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3324"
  - "gspC"
---

# gspC

`gene.b3324`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3324`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspC (gene.b3324) is a gene entity. It encodes gspC (protein.P45757). Encoded protein function: FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of proteins. {ECO:0000305}. EcoCyc product frame: G7702-MONOMER. EcoCyc synonyms: yheE. Genomic coordinates: 3455578-3456393. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . GspC is predicted to be a bitopic inner membrane protein . gspC encodes the inner membrane platform protein of gram-negative type II secretion systems (see ). gsp: general secretory pathway (and see )

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45757|protein.P45757]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspC; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspC; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspC; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010877,ECOCYC:G7702,GeneID:947824`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3455578-3456393:+; feature_type=gene
