---
entity_id: "gene.b1349"
entity_type: "gene"
name: "recT"
source_database: "NCBI RefSeq"
source_id: "gene-b1349"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1349"
  - "recT"
---

# recT

`gene.b1349`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1349`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recT (gene.b1349) is a gene entity. It encodes recT (protein.P33228). Encoded protein function: FUNCTION: Binds to single-stranded DNA and also promotes the renaturation of complementary single-stranded DNA. Function in recombination. Has a function similar to that of lambda RedB. EcoCyc product frame: EG11899-MONOMER. Genomic coordinates: 1413984-1414793. EcoCyc protein note: The Rac prophage of E. coli encodes two proteins of the ATP-independent RecE recombination pathway involved in homologous pairing and strand exchange. Under certain conditions RecE and RecT can act in place of RecA as a homologous pairing, strand-exchange recombination system. The overlapping recE and recT genes encode proteins involved in RecE-mediated double strand break (DSB) repair, and are activated in recBC sbcA mutants. RecE and RecT were shown to interact directly . Both RecE and RecT were required for double-strand break repair in a recBC sbcA background . The RecE protein creates 3' overhangs from double-strand breaks and RecT anneals them with homologous DNA and promotes strand exchange . RecT is able to substitute for λ red β in λ recombination . RecT was shown to promote the renaturation of homologous ssDNA . RecT promotes the formation of joint molecules of supercoiled DNA with exonuclease-resected dsDNA having 5' homologous single-stranded ends...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33228|protein.P33228]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004529,ECOCYC:EG11899,GeneID:945917`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1413984-1414793:-; feature_type=gene
