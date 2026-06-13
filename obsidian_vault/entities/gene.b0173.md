---
entity_id: "gene.b0173"
entity_type: "gene"
name: "dxr"
source_database: "NCBI RefSeq"
source_id: "gene-b0173"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0173"
  - "dxr"
---

# dxr

`gene.b0173`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0173`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dxr (gene.b0173) is a gene entity. It encodes dxr (protein.P45568). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol 4-phosphate (MEP). {ECO:0000269|PubMed:10631325, ECO:0000269|PubMed:10787409, ECO:0000269|PubMed:9707569}. EcoCyc product frame: DXPREDISOM-MONOMER. EcoCyc synonyms: yaeM, ispC. Genomic coordinates: 193521-194717.

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45568|protein.P45568]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000592,ECOCYC:EG12715,GeneID:945019`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:193521-194717:+; feature_type=gene
