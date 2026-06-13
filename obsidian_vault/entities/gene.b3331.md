---
entity_id: "gene.b3331"
entity_type: "gene"
name: "gspJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3331"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3331"
  - "gspJ"
---

# gspJ

`gene.b3331`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3331`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspJ (gene.b3331) is a gene entity. It encodes gspJ (protein.P45761). Encoded protein function: FUNCTION: Component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Part of the pseudopilus tip complex that is critical for the recognition and binding of secretion substrates. {ECO:0000250|UniProtKB:Q00517}. EcoCyc product frame: G7709-MONOMER. EcoCyc synonyms: yheI. Genomic coordinates: 3462344-3462931. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspJ encodes a minor pseudopilin of gram-negative type II secretion systems (see ). GspJ is predicted to be a bitopic inner membrane protein . gsp: general secretory pathway

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45761|protein.P45761]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspJ; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspJ; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspJ; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010892,ECOCYC:G7709,GeneID:947832`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3462344-3462931:+; feature_type=gene
