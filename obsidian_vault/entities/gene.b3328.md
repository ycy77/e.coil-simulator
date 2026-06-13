---
entity_id: "gene.b3328"
entity_type: "gene"
name: "gspG"
source_database: "NCBI RefSeq"
source_id: "gene-b3328"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3328"
  - "gspG"
---

# gspG

`gene.b3328`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3328`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspG (gene.b3328) is a gene entity. It encodes gspG (protein.P41442). Encoded protein function: FUNCTION: Core component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Pseudopilin (pilin-like) protein that polymerizes to form the pseudopilus. Further polymerization triggers pseudopilus growth. {ECO:0000250|UniProtKB:Q00514}. EcoCyc product frame: G7706-MONOMER. EcoCyc synonyms: hofG, hopG. Genomic coordinates: 3461023-3461460. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . GspG is predicted to be a bitopic inner membrane protein . gspG encodes the major pseudopilin of gram-negative type II secretion systems (see ). gspG was significantly upregulated in simulated microgravity . gsp: general secretory pathway hopG: homology with PulG, OutG and ExeG (see )

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8), nac (protein.Q47005). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41442|protein.P41442]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspG; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspG; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspG; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspG; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gspG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010885,ECOCYC:G7706,GeneID:947827`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3461023-3461460:+; feature_type=gene
