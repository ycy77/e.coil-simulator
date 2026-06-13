---
entity_id: "gene.b1046"
entity_type: "gene"
name: "clsC"
source_database: "NCBI RefSeq"
source_id: "gene-b1046"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1046"
  - "clsC"
---

# clsC

`gene.b1046`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1046`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clsC (gene.b1046) is a gene entity. It encodes clsC (protein.P75919). Encoded protein function: FUNCTION: Catalyzes the synthesis of cardiolipin (CL) (diphosphatidylglycerol) from phosphatidylglycerol (PG) and phosphatidylethanolamine (PE). {ECO:0000269|PubMed:22988102}. EcoCyc product frame: G6551-MONOMER. EcoCyc synonyms: ymdC. Genomic coordinates: 1106355-1107776. EcoCyc protein note: ClsC is a third cardiolipin synthase in E. coli. Synthesis of cardiolipin during exponential growth is due to the activity of CARDIOLIPSYN-MONOMER ClsA, while all three cardiolipin synthases, ClsA, G6406-MONOMER ClsB and ClsC, contribute to cardiolipin synthesis in stationary phase . Full complementation of a clsC mutant requires co-expression with G6550, the gene directly upstream of clsC. However, more recent studies using plasmids with various lengths of nucleotides upstream of the currently annotated TTG start site found that the ATG +9 nucleotides upstream is most likely the true start site for transcription of clsC; the ymdB gene was not required. Additionally, using a thin layer chromatography-based assay with P32 found the ClsC (+9 bp ATG) produced the P32-labelled cardiolipin, and ymdB was not required for phosphatidylethanolamine substrate specificity . Cells with deletions of all three of the genes encoding cardiolipin synthases, ΔclsABC, completely lack cardiolipin...

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75919|protein.P75919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003551,ECOCYC:G6551,GeneID:947321`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1106355-1107776:+; feature_type=gene
