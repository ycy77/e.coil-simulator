---
entity_id: "gene.b0011"
entity_type: "gene"
name: "yaaW"
source_database: "NCBI RefSeq"
source_id: "gene-b0011"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0011"
  - "yaaW"
---

# yaaW

`gene.b0011`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0011`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaaW (gene.b0011) is a gene entity. It encodes yaaW (protein.P75617). Encoded protein function: UPF0174 protein YaaW EcoCyc product frame: G6082-MONOMER. Genomic coordinates: 10643-11356. EcoCyc protein note: Mutagenesis experiments performed to study the htgA open reading frame on the opposite strand indicated that HtgA may play a role in the regulation of the heat shock response . However, all mutagenesis experiments disrupted both htgA and yaaW. Experiments using the E. coli O157:H7 EDL933 yaaW and htgA genes, which are more than 98% identical to those of E. coli K-12, are reported in . yaaW is most likely part of an yaaIWH operon. Point mutants that selectively knock out either yaaW or htgA were constructed and tested. Neither mutant has a heat shock phenotype, and both mutants show somewhat increased biofilm formation in minimal medium after 48 hours . have suggested that the antisense htgA ORF has originated through overprinting and have proposed the term "janolog" to describe such events.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75617|protein.P75617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000037,ECOCYC:G6082,GeneID:944771`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:10643-11356:-; feature_type=gene
