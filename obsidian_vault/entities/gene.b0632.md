---
entity_id: "gene.b0632"
entity_type: "gene"
name: "dacA"
source_database: "NCBI RefSeq"
source_id: "gene-b0632"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0632"
  - "dacA"
---

# dacA

`gene.b0632`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0632`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dacA (gene.b0632) is a gene entity. It encodes dacA (protein.P0AEB2). Encoded protein function: FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors. EcoCyc product frame: EG10201-MONOMER. EcoCyc synonyms: pfv. Genomic coordinates: 662752-663963.

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEB2|protein.P0AEB2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002168,ECOCYC:EG10201,GeneID:945222`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:662752-663963:-; feature_type=gene
