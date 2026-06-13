---
entity_id: "gene.b0753"
entity_type: "gene"
name: "ybgS"
source_database: "NCBI RefSeq"
source_id: "gene-b0753"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0753"
  - "ybgS"
---

# ybgS

`gene.b0753`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0753`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgS (gene.b0753) is a gene entity. It encodes ybgS (protein.P0AAV6). Encoded protein function: Uncharacterized protein YbgS EcoCyc product frame: G6394-MONOMER. Genomic coordinates: 784937-785317. EcoCyc protein note: A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAV6|protein.P0AAV6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002553,ECOCYC:G6394,GeneID:945356`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:784937-785317:-; feature_type=gene
