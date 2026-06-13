---
entity_id: "gene.b0761"
entity_type: "gene"
name: "modE"
source_database: "NCBI RefSeq"
source_id: "gene-b0761"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0761"
  - "modE"
---

# modE

`gene.b0761`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0761`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

modE (gene.b0761) is a gene entity. It encodes modE (protein.P0A9G8). Encoded protein function: FUNCTION: Functions as an intracellular molybdate sensor. The ModE-Mo complex acts as a repressor of the modABC operon, which is involved in the transport of molybdate (PubMed:8550508). Binds modA promoter DNA in the absence of molybdate, however molybdate binding confers increased DNA affinity (PubMed:9044285, PubMed:9210473). Binds the promoter of moaA activating its transcription; binding is not enhanced by molybdate (PubMed:9044285). The protein dimer binds the consensus palindrome sequence 5'-TATAT-N7-TAYAT-3' and a variant 5'-TGTGT-N7-TGYGT-3' (PubMed:16205910, PubMed:9044285, PubMed:9210473). Acts as a regulator of the expression of 67 genes, many of which encode molybdoenzymes, acts both directly and indirectly (PubMed:10206709, PubMed:16205910, PubMed:9466267). ModE also binds tungstate (PubMed:11259434, PubMed:9210473). {ECO:0000269|PubMed:10206709, ECO:0000269|PubMed:11259434, ECO:0000269|PubMed:16205910, ECO:0000269|PubMed:8550508, ECO:0000269|PubMed:9044285, ECO:0000269|PubMed:9210473, ECO:0000269|PubMed:9466267}. EcoCyc product frame: MONOMER0-185. EcoCyc synonyms: chlD, modR. Genomic coordinates: 793856-794644.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9G8|protein.P0A9G8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002585,ECOCYC:G6395,GeneID:945366`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:793856-794644:-; feature_type=gene
