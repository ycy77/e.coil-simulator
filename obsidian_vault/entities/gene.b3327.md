---
entity_id: "gene.b3327"
entity_type: "gene"
name: "gspF"
source_database: "NCBI RefSeq"
source_id: "gene-b3327"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3327"
  - "gspF"
---

# gspF

`gene.b3327`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3327`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspF (gene.b3327) is a gene entity. It encodes gspF (protein.P41441). Encoded protein function: FUNCTION: Component of the type II secretion system inner membrane complex required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. {ECO:0000250|UniProtKB:Q00514}. EcoCyc product frame: G7705-MONOMER. EcoCyc synonyms: hofF, hopF. Genomic coordinates: 3459817-3461013. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspF encodes a component of the inner membrane platform of gram-negative type II secretion systems (see ). gsp: general secretory pathway hopF: homology with PulF (see )

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41441|protein.P41441]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspF; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspF; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspF; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010883,ECOCYC:G7705,GeneID:947829`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3459817-3461013:+; feature_type=gene
