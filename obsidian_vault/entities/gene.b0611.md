---
entity_id: "gene.b0611"
entity_type: "gene"
name: "rna"
source_database: "NCBI RefSeq"
source_id: "gene-b0611"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0611"
  - "rna"
---

# rna

`gene.b0611`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0611`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rna (gene.b0611) is a gene entity. It encodes rna (protein.P21338). Encoded protein function: FUNCTION: One of the few RNases that cleaves the phosphodiester bond between any two nucleotide. Shows a preference for cytidylic or guanylic acid. EcoCyc product frame: EG10856-MONOMER. EcoCyc synonyms: rnsA. Genomic coordinates: 644197-645003. EcoCyc protein note: Ribonuclease I (RNase I) is an endoribonuclease that cleaves phosphodiester bonds between any two nucleotides in RNA, yielding nucleoside 3'-phosphates and 3'-phosphooligonucleotides . RNase I is partially responsible for the degradation of total and ribosomal RNA during both normal and nutrient starvation conditions, especially during carbon starvation . RNase I is specifically required for the breakdown of 23S RNA, though it is not required for degradation of 16S RNA or very small (4S) RNA fragments that result from breakdown of larger RNA . RNase I degradation of the 50S ribosomal subunit releases the ribosomal proteins L4, L10 and L7/12 in addition to cleaving the 23S RNA to yield a smaller product . Polyamines stimulate the activity of RNase I against synthetic polynucleotides in vitro . RNase I is primarily a periplasmic protein that can be released by spheroblasting or treatment of cells with N-dodecyldiethanolamine. The latter treatment allows subsequent enhanced breakdown of rRNA by RNase I...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21338|protein.P21338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002107,ECOCYC:EG10856,GeneID:949065`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:644197-645003:-; feature_type=gene
