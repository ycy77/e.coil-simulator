---
entity_id: "gene.b3448"
entity_type: "gene"
name: "yhhA"
source_database: "NCBI RefSeq"
source_id: "gene-b3448"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3448"
  - "yhhA"
---

# yhhA

`gene.b3448`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3448`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhhA (gene.b3448) is a gene entity. It encodes yhhA (protein.P0ADX7). Encoded protein function: Uncharacterized protein YhhA (ORFQ) EcoCyc product frame: EG11184-MONOMER. Genomic coordinates: 3586943-3587383. EcoCyc protein note: A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADX7|protein.P0ADX7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011262,ECOCYC:EG11184,GeneID:947956`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3586943-3587383:+; feature_type=gene
