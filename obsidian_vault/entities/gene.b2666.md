---
entity_id: "gene.b2666"
entity_type: "gene"
name: "yqaE"
source_database: "NCBI RefSeq"
source_id: "gene-b2666"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2666"
  - "yqaE"
---

# yqaE

`gene.b2666`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2666`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqaE (gene.b2666) is a gene entity. It encodes yqaE (protein.P0AE42). Encoded protein function: PMP3 family protein YqaE EcoCyc product frame: G7396-MONOMER. Genomic coordinates: 2796870-2797028. EcoCyc protein note: YqaE is a predicted membrane protein of unknown function. A Phenotype MicroArray analysis performed with a yqaE null mutant showed that the mutant strain gains resistance to a variety of antibiotics . yqaE and ygaU may form a Cpx-P induced transcription unit . yqaE expression is induced by CpxR and is negatively regulated at the posttranscriptional level by the small RNA CyaR . Transcription of yqaE may be regulated by the alternative sigma factor σS under certain stress conditions . A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress .

## Biological Role

Repressed by cyaR (gene.b4438). Activated by cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE42|protein.P0AE42]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=yqaE; function=+
- `represses` <-- [[gene.b4438|gene.b4438]] `RegulonDB` `S` - regulator=CyaR; target=yqaE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008770,ECOCYC:G7396,GeneID:947138`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2796870-2797028:-; feature_type=gene
