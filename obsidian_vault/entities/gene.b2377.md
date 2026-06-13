---
entity_id: "gene.b2377"
entity_type: "gene"
name: "yfdY"
source_database: "NCBI RefSeq"
source_id: "gene-b2377"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2377"
  - "yfdY"
---

# yfdY

`gene.b2377`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2377`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdY (gene.b2377) is a gene entity. It encodes yfdY (protein.P76521). Encoded protein function: Uncharacterized protein YfdY EcoCyc product frame: G7240-MONOMER. Genomic coordinates: 2495050-2495292. EcoCyc protein note: Expression of yfdY is induced upon biofilm formation . Overexpression of yfdY from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid . A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress .

## Biological Role

Activated by DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76521|protein.P76521]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007841,ECOCYC:G7240,GeneID:948842`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2495050-2495292:-; feature_type=gene
