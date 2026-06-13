---
entity_id: "gene.b3332"
entity_type: "gene"
name: "gspK"
source_database: "NCBI RefSeq"
source_id: "gene-b3332"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3332"
  - "gspK"
---

# gspK

`gene.b3332`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3332`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspK (gene.b3332) is a gene entity. It encodes gspK (protein.P45762). Encoded protein function: FUNCTION: Component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Plays a role in pseudopilus assembly and seems to control its length. Interacts with the pseudopilus tip complex that is critical for the recognition and binding of secretion substrates. {ECO:0000250|UniProtKB:Q00518}. EcoCyc product frame: G7710-MONOMER. EcoCyc synonyms: yheJ. Genomic coordinates: 3462924-3463907. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspK encodes a minor pseudopilin of gram-negative type II secretion systems (see ). GspK is predicted to be a bitopic inner membrane protein . gsp: general secretory pathway

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45762|protein.P45762]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspK; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspK; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspK; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010894,ECOCYC:G7710,GeneID:947831`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3462924-3463907:+; feature_type=gene
