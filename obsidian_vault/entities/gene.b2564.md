---
entity_id: "gene.b2564"
entity_type: "gene"
name: "pdxJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2564"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2564"
  - "pdxJ"
---

# pdxJ

`gene.b2564`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2564`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdxJ (gene.b2564) is a gene entity. It encodes pdxJ (protein.P0A794). Encoded protein function: FUNCTION: Catalyzes the complicated ring closure reaction between the two acyclic compounds 1-deoxy-D-xylulose-5-phosphate (DXP) and 3-amino-2-oxopropyl phosphate (1-amino-acetone-3-phosphate or AAP) to form pyridoxine 5'-phosphate (PNP) and inorganic phosphate. {ECO:0000269|PubMed:10225425}. EcoCyc product frame: PDXJ-MONOMER. Genomic coordinates: 2700998-2701729. EcoCyc protein note: Pyridoxine 5'-phosphate synthase (PdxJ) is one of the key enzymes in de novo pyridoxine 5'-phosphate synthesis. It catalyzes a complicated ring-closure reaction involving the condensation of 1-deoxy-D-xylulose 5-phosphate (DXP) and 3-amino-1-hydroxyacetone 1-phosphate to form pyridoxine 5'-phosphate (PNP) . Crystal structures of PdxJ have been solved . The enzyme is an octamer in solution . The octamer is organized as a tetramer of active dimers; each monomer consists of a (β/α)8 TIM barrel domain. Structures of enzyme/substrate and enzyme/product complexes allowed localization of the active site within a deep cavity which is closed in the presence of the product . Each subunit of the octamer has a unique conformation that is correlated with the occupancy of the active site. The substrate-binding sites are located at the interface of two subunits...

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A794|protein.P0A794]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008435,ECOCYC:EG10693,GeneID:947039`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2700998-2701729:-; feature_type=gene
