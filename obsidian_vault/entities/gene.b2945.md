---
entity_id: "gene.b2945"
entity_type: "gene"
name: "endA"
source_database: "NCBI RefSeq"
source_id: "gene-b2945"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2945"
  - "endA"
---

# endA

`gene.b2945`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2945`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

endA (gene.b2945) is a gene entity. It encodes endA (protein.P25736). Encoded protein function: FUNCTION: Has double-strand break activity. EcoCyc product frame: EG11336-MONOMER. Genomic coordinates: 3090347-3091054. EcoCyc protein note: Endonuclease I is a periplasmic enzyme that cleaves within duplex DNA. Its cellular role is unknown. Endonuclease I cleaves within duplex DNA, producing oligonucleotides that are on average 7 bp long and contain 5' phosphate groups . It is inhibited by tRNA and rRNA . Even though it was originally reported that mutants lacking endA show no apparent difference from wild type cells , several phenotypes were reported later. An endA deletion strain is sensitive to CPD0-1392 , and deletion of endA was found to facilitate plasmid isolation from E. coli strains . A UV-resistant mutant increased DNA polymerase I and endonuclease I activity . EndA: endonuclease I .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25736|protein.P25736]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009661,ECOCYC:EG11336,GeneID:949092`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3090347-3091054:+; feature_type=gene
