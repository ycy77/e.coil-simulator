---
entity_id: "gene.b2141"
entity_type: "gene"
name: "yohJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2141"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2141"
  - "yohJ"
---

# yohJ

`gene.b2141`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2141`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yohJ (gene.b2141) is a gene entity. It encodes yohJ (protein.P60632). Encoded protein function: UPF0299 membrane protein YohJ EcoCyc product frame: EG12023-MONOMER. Genomic coordinates: 2230624-2231022. EcoCyc protein note: yohJ and yohK encode two inner membrane proteins implicated in the export of 3-HYDROXY-PROPIONATE (3-HP) . yohJK belongs to the EG11733-MONOMER YieP regulon; YieP downregulates expression of yohJK; deletion of yieP improves tolerance to 3-HP in a number of E. coli strains including K-12 . The growth of an E. coli W ΔyohJK mutant is significantly reduced in the presence of 300mM 3-HP; over-expression of yohJK (in E. coli W) improves tolerance to 3-HP; the intracellular concentration of 3-HP is significantly reduced when yieP is deleted or when yohJK is overexpressed . YohJ is predicted to be an inner membrane protein with four transmembrane domains; experimental topology analysis suggests the C-terminus is located in the periplasm .

## Biological Role

Repressed by yieP (protein.P31475).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60632|protein.P60632]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P31475|protein.P31475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007078,ECOCYC:EG12023,GeneID:949127`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2230624-2231022:+; feature_type=gene
