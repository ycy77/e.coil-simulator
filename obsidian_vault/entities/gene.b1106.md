---
entity_id: "gene.b1106"
entity_type: "gene"
name: "thiK"
source_database: "NCBI RefSeq"
source_id: "gene-b1106"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1106"
  - "thiK"
---

# thiK

`gene.b1106`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1106`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiK (gene.b1106) is a gene entity. It encodes thiK (protein.P75948). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of thiamine to thiamine phosphate. Is involved in thiamine salvage. {ECO:0000269|PubMed:15150256}. EcoCyc product frame: THIKIN-MONOMER. EcoCyc synonyms: ycfN. Genomic coordinates: 1163260-1164084. EcoCyc protein note: Thiamine kinase (ThiK) catalyzes the phosphorylation of the hydroxyl group of thiamin. This enzyme is a salvage enzyme and enables the cell to use recycled thiamin as an alternative to its synthesis de novo. The thiK locus was mapped , and the ycfN open reading frame was identified as the structural gene encoding thiamine kinase. The gene was overexpressed as a His10-tagged protein, but the protein was present primarily in inclusion bodies, was unstable, and lost all activity during purification, although assays performed with cell extracts showed significant thiamine kinase activity . The Keio collection thiK mutant is sensitive to lithium (<90% growth at 100mM Li) . Orthologs of ThiK have so far only been found in the γ proteobacteria.

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75948|protein.P75948]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003735,ECOCYC:G6566,GeneID:948525`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1163260-1164084:+; feature_type=gene
