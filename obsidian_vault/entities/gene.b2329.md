---
entity_id: "gene.b2329"
entity_type: "gene"
name: "aroC"
source_database: "NCBI RefSeq"
source_id: "gene-b2329"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2329"
  - "aroC"
---

# aroC

`gene.b2329`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2329`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroC (gene.b2329) is a gene entity. It encodes aroC (protein.P12008). Encoded protein function: FUNCTION: Catalyzes the anti-1,4-elimination of the C-3 phosphate and the C-6 proR hydrogen from 5-enolpyruvylshikimate-3-phosphate (EPSP) to yield chorismate, which is the branch point compound that serves as the starting substrate for the three terminal pathways of aromatic amino acid biosynthesis. This reaction introduces a second double bond into the aromatic ring system. It uses NADPH to reduce FMN. {ECO:0000255|HAMAP-Rule:MF_00300, ECO:0000269|PubMed:10956653, ECO:0000269|PubMed:11034781, ECO:0000269|PubMed:2969724, ECO:0000269|PubMed:7848266, ECO:0000269|PubMed:7978236, ECO:0000269|PubMed:8703965}. EcoCyc product frame: AROC-MONOMER. Genomic coordinates: 2446388-2447473. EcoCyc protein note: Chorismate synthase (AroC) is involved in the 7th and last step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. This enzyme catalyzes the conversion of 5-enolpyruvylshikimate 3-phosphate into chorismate, which is the branch point compound that serves as the starting substrate for the three terminal pathways of aromatic amino acid biosynthesis. This reaction introduces a second double bond into the aromatic ring system. The enzymatic mechanism has been studied in detail...

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12008|protein.P12008]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007693,ECOCYC:EG10075,GeneID:946814`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2446388-2447473:-; feature_type=gene
