---
entity_id: "gene.b1266"
entity_type: "gene"
name: "rnm"
source_database: "NCBI RefSeq"
source_id: "gene-b1266"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1266"
  - "rnm"
---

# rnm

`gene.b1266`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1266`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnm (gene.b1266) is a gene entity. It encodes rnm (protein.P77766). Encoded protein function: FUNCTION: Exoribonuclease that catalyzes the last steps of 5S, 16S and 23S rRNA 5'-end maturation. Removes 3 nucleotides (nt) from the 5' end of 5S, 16S and 23S rRNA precursors to generate the mature 5' ends. Precursors with longer extensions are not processed (7 nt at the 5' end of pre-23S rRNA or 66 nt at the 5'-end of 16S rRNA are not processed). 5S and 23S rRNA maturation occurs more efficiently and accurately on ribosomal particles as compared to free RNA; the enzyme overdigests free RNA but generates the correct 5'-end in ribosomes from rnm deletion strains (PubMed:32343306). Efficiently catalyzes the hydrolysis of the 3'-phosphate from 3',5'-bis-phosphonucleotides as well as the successive hydrolysis of 5'-phosphomononucleotides from the 5'-end of short pieces of RNA and DNA, with no specificity toward the identity of the nucleotide base. Is more efficient at hydrolyzing RNA oligonucleotides than DNA oligonucleotides. This enzyme can also hydrolyze annealed DNA duplexes, albeit at a catalytic efficiency approximately 10-fold lower than that of the corresponding single-stranded oligonucleotides. {ECO:0000269|PubMed:25871919, ECO:0000269|PubMed:32343306}. EcoCyc product frame: G6634-MONOMER. EcoCyc synonyms: trpH, yciV. Genomic coordinates: 1323220-1324101...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77766|protein.P77766]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004252,ECOCYC:G6634,GeneID:945857`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1323220-1324101:+; feature_type=gene
