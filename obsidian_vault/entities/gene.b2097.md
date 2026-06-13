---
entity_id: "gene.b2097"
entity_type: "gene"
name: "fbaB"
source_database: "NCBI RefSeq"
source_id: "gene-b2097"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2097"
  - "fbaB"
---

# fbaB

`gene.b2097`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2097`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fbaB (gene.b2097) is a gene entity. It encodes fbaB (protein.P0A991). Encoded protein function: FUNCTION: Catalyzes the reversible aldol condensation/cleavage reaction between glyceraldehyde 3-phosphate and dihydroxyacetone phosphate (DHAP) to yield fructose-bisphosphate (FBP). {ECO:0000269|PubMed:9531482}. EcoCyc product frame: FRUCBISALD-CLASSI-MONOMER. EcoCyc synonyms: dhnA. Genomic coordinates: 2177512-2178564.

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A991|protein.P0A991]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=fbaB; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=fbaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006941,ECOCYC:G7129,GeneID:946632`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2177512-2178564:-; feature_type=gene
