---
entity_id: "gene.b3326"
entity_type: "gene"
name: "gspE"
source_database: "NCBI RefSeq"
source_id: "gene-b3326"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3326"
  - "gspE"
---

# gspE

`gene.b3326`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3326`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspE (gene.b3326) is a gene entity. It encodes gspE (protein.P45759). Encoded protein function: FUNCTION: ATPase component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Acts as a molecular motor to provide the energy that is required for assembly of the pseudopilus and the extrusion of substrates generated in the cytoplasm. {ECO:0000250|UniProtKB:Q00512}. EcoCyc product frame: G7704-MONOMER. EcoCyc synonyms: yheG. Genomic coordinates: 3458339-3459820. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspE encodes the cytoplasmic ATPase of gram-negative type II secretion systems (see ). gsp: general secretory pathway

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45759|protein.P45759]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspE; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspE; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspE; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010881,ECOCYC:G7704,GeneID:947823`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3458339-3459820:+; feature_type=gene
