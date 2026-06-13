---
entity_id: "gene.b3998"
entity_type: "gene"
name: "nfi"
source_database: "NCBI RefSeq"
source_id: "gene-b3998"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3998"
  - "nfi"
---

# nfi

`gene.b3998`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3998`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfi (gene.b3998) is a gene entity. It encodes nfi (protein.P68739). Encoded protein function: FUNCTION: DNA repair enzyme involved in the repair of deaminated bases. Selectively cleaves double-stranded DNA at the second phosphodiester bond 3' to a deoxyinosine leaving behind the intact lesion on the nicked DNA. Has a wide substrate spectrum. In addition to deoxyinosine-containing DNA, the enzyme cleaves DNA containing urea residues, AP sites, base mismatches, insertion/deletion mismatches, flaps, and pseudo-Y structures. Participates in the excision repair of hypoxanthine and xanthine (deaminated adenine and guanine) in DNA. It thereby reduces the mutagenic effects of nitrous acid by attacking lesions caused by nitrosative deamination. Also active on inosines in single- and double-stranded RNA. May cleave tRNA(Arg2), which contains inosine at the wobble position. {ECO:0000255|HAMAP-Rule:MF_00801, ECO:0000269|PubMed:11104906, ECO:0000269|PubMed:23912683, ECO:0000269|PubMed:6246346, ECO:0000269|PubMed:8206931, ECO:0000269|PubMed:9388217}. EcoCyc product frame: EG11915-MONOMER. EcoCyc synonyms: yjaF. Genomic coordinates: 4198790-4199461...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68739|protein.P68739]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:EG11915,GeneID:948502`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4198790-4199461:+; feature_type=gene
