---
entity_id: "gene.b3919"
entity_type: "gene"
name: "tpiA"
source_database: "NCBI RefSeq"
source_id: "gene-b3919"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3919"
  - "tpiA"
---

# tpiA

`gene.b3919`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3919`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tpiA (gene.b3919) is a gene entity. It encodes tpiA (protein.P0A858). Encoded protein function: FUNCTION: Involved in the gluconeogenesis. Catalyzes stereospecifically the conversion of dihydroxyacetone phosphate (DHAP) to D-glyceraldehyde-3-phosphate (G3P). {ECO:0000255|HAMAP-Rule:MF_00147, ECO:0000269|PubMed:9442062}. EcoCyc product frame: TPI-MONOMER. EcoCyc synonyms: tpi. Genomic coordinates: 4110740-4111507.

## Biological Role

Repressed by cra (protein.P0ACP1).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A858|protein.P0A858]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=tpiA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012799,ECOCYC:EG11015,GeneID:948409`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4110740-4111507:-; feature_type=gene
