---
entity_id: "gene.b3329"
entity_type: "gene"
name: "gspH"
source_database: "NCBI RefSeq"
source_id: "gene-b3329"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3329"
  - "gspH"
---

# gspH

`gene.b3329`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3329`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspH (gene.b3329) is a gene entity. It encodes gspH (protein.P41443). Encoded protein function: FUNCTION: Component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Part of the pseudopilus tip complex that is critical for the recognition and binding of secretion substrates. {ECO:0000250|UniProtKB:Q00515}. EcoCyc product frame: G7707-MONOMER. EcoCyc synonyms: hofH, hopH. Genomic coordinates: 3461468-3461977. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspH encodes a minor pseudopilin of gram-negative type II secretion systems (see ). gsp: general secretory pathway hopH: homology with PulH (see )

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8), nac (protein.Q47005). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41443|protein.P41443]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspH; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspH; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspH; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspH; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gspH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010888,ECOCYC:G7707,GeneID:947834`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3461468-3461977:+; feature_type=gene
