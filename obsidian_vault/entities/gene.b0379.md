---
entity_id: "gene.b0379"
entity_type: "gene"
name: "yaiY"
source_database: "NCBI RefSeq"
source_id: "gene-b0379"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0379"
  - "yaiY"
---

# yaiY

`gene.b0379`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0379`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaiY (gene.b0379) is a gene entity. It encodes yaiY (protein.P0AAP7). Encoded protein function: Inner membrane protein YaiY EcoCyc product frame: G6228-MONOMER. Genomic coordinates: 399025-399333. EcoCyc protein note: YaiY localizes to the inner membrane. YaiY is predicted to contain two transmembrane domains; the C terminus is located in the cytoplasm . A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress .

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAP7|protein.P0AAP7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yaiY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001302,ECOCYC:G6228,GeneID:945223`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:399025-399333:-; feature_type=gene
