---
entity_id: "gene.b4025"
entity_type: "gene"
name: "pgi"
source_database: "NCBI RefSeq"
source_id: "gene-b4025"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4025"
  - "pgi"
---

# pgi

`gene.b4025`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4025`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgi (gene.b4025) is a gene entity. It encodes pgi (protein.P0A6T1). Encoded protein function: FUNCTION: Catalyzes the reversible isomerization of glucose-6-phosphate to fructose-6-phosphate. {ECO:0000255|HAMAP-Rule:MF_00473}. EcoCyc product frame: PGLUCISOM. Genomic coordinates: 4233758-4235407.

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6T1|protein.P0A6T1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=pgi; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=pgi; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013163,ECOCYC:EG10702,GeneID:948535`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4233758-4235407:+; feature_type=gene
