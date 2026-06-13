---
entity_id: "gene.b3437"
entity_type: "gene"
name: "gntK"
source_database: "NCBI RefSeq"
source_id: "gene-b3437"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3437"
  - "gntK"
---

# gntK

`gene.b3437`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3437`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gntK (gene.b3437) is a gene entity. It encodes gntK (protein.P46859). Encoded protein function: Thermoresistant gluconokinase (EC 2.7.1.12) (Gluconate kinase 2) EcoCyc product frame: GLUCONOKINII-MONOMER. Genomic coordinates: 3577065-3577592.

## Biological Role

Repressed by gntR (protein.P0ACP5). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46859|protein.P46859]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gntK; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gntK; function=+
- `represses` <-- [[protein.P0ACP5|protein.P0ACP5]] `RegulonDB` `C` - regulator=GntR; target=gntK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011224,ECOCYC:EG12629,GeneID:947937`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3577065-3577592:-; feature_type=gene
