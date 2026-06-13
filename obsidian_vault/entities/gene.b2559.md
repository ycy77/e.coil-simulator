---
entity_id: "gene.b2559"
entity_type: "gene"
name: "tadA"
source_database: "NCBI RefSeq"
source_id: "gene-b2559"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2559"
  - "tadA"
---

# tadA

`gene.b2559`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2559`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tadA (gene.b2559) is a gene entity. It encodes tadA (protein.P68398). Encoded protein function: FUNCTION: Catalyzes the deamination of adenosine to inosine at the wobble position 34 of tRNA(Arg2). Essential for cell viability. {ECO:0000255|HAMAP-Rule:MF_00972, ECO:0000269|PubMed:12110595, ECO:0000269|PubMed:16700551}. EcoCyc product frame: EG11372-MONOMER. EcoCyc synonyms: yfhC. Genomic coordinates: 2697354-2697857. EcoCyc protein note: tRNA adenosine34 deaminase (TadA) belongs to the family of adenosine deaminases of tRNA (ADATs). It catalyzes deamination of adenosine to inosine at position 34, the wobble base of the anticodon loop, of tRNAArg2. Substrate requirements have been evaluated; the anticodon stem and loop are found to be sufficient for inosine formation . Surprisingly, a small number of mRNAs are also targets for A-to-I editing in E. coli, and TadA was identified as the responsible enzyme. One of the edited mRNAs is G0-9610 hokB, which encodes a small toxic protein. Because inosine is recognized as guanine by the translation machinery, editing of hokB mRNA changes a tyrosine (TAC) codon into a cysteine (TGC) codon at position 29. The predicted secondary structure of the hokB mRNA resembles that of an anticodon stem-loop, with the edited nucleotide positioned in the loop . TadA forms a homodimer . A crystal structure of TadA has been solved at 2.0 Å resolution...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68398|protein.P68398]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008419,ECOCYC:EG11372,GeneID:947027`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2697354-2697857:-; feature_type=gene
