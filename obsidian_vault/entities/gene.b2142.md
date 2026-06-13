---
entity_id: "gene.b2142"
entity_type: "gene"
name: "yohK"
source_database: "NCBI RefSeq"
source_id: "gene-b2142"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2142"
  - "yohK"
---

# yohK

`gene.b2142`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2142`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yohK (gene.b2142) is a gene entity. It encodes yohK (protein.P0AD19). Encoded protein function: Inner membrane protein YohK EcoCyc product frame: EG12024-MONOMER. Genomic coordinates: 2231019-2231714. EcoCyc protein note: yohJ and yohK encode two inner membrane proteins implicated in the export of 3-HYDROXY-PROPIONATE (3-HP) . yohJK belongs to the EG11733-MONOMER YieP regulon; YieP downregulates expression of yohJK; deletion of yieP improves tolerance to 3-HP in a number of E. coli strains including K-12 . The growth of an E. coli W ΔyohJK mutant is significantly reduced in the presence of 300mM 3-HP; over-expression of yohJK (in E. coli W) improves tolerance to 3-HP; the intracellular concentration of 3-HP is significantly reduced when yieP is deleted or when yohJK is overexpressed . YohK is predicted to be an inner membrane protein with six transmembrane domains; experimental topology analysis suggests the C-terminus is located in the periplasm .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD19|protein.P0AD19]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007080,ECOCYC:EG12024,GeneID:949125`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2231019-2231714:+; feature_type=gene
