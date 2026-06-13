---
entity_id: "gene.b3333"
entity_type: "gene"
name: "gspL"
source_database: "NCBI RefSeq"
source_id: "gene-b3333"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3333"
  - "gspL"
---

# gspL

`gene.b3333`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3333`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspL (gene.b3333) is a gene entity. It encodes gspL (protein.P45763). Encoded protein function: FUNCTION: Inner membrane component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Plays a role in the complex assembly and recruits GspM resulting in a stable complex in the inner membrane. Provides thus a link between the energy-providing GspE protein in the cytoplasm and the rest of the T2SS machinery. {ECO:0000250|UniProtKB:P25060}. EcoCyc product frame: G7711-MONOMER. EcoCyc synonyms: yheK. Genomic coordinates: 3463922-3465085. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspL encodes a component of the inner membrane platform of gram-negative type II secretion systems (see ). gsp: general secretory pathway

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45763|protein.P45763]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspL; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspL; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspL; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010896,ECOCYC:G7711,GeneID:947842`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3463922-3465085:+; feature_type=gene
