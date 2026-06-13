---
entity_id: "gene.b1824"
entity_type: "gene"
name: "yobF"
source_database: "NCBI RefSeq"
source_id: "gene-b1824"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1824"
  - "yobF"
---

# yobF

`gene.b1824`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1824`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yobF (gene.b1824) is a gene entity. It encodes yobF (protein.P64508). Encoded protein function: Protein YobF EcoCyc product frame: G7000-MONOMER. Genomic coordinates: 1907448-1907591. EcoCyc protein note: YobF is a small protein that belongs to the DUF2527 family of proteins of unknown function. YobF expression is post-transcriptionally regulated by the RYEE-RNA . yobF was predicted to be a target of the OXYS-RNA. Overexpression of OxyS decreases the expression of yobF . YobF is expressed during stationary phase . Levels of YobF protein increases after heat shock; induction occurs at the post-transcriptional level . In growth competition experiments, a yobF deletion mutant is more sensitive to cell envelope stress and acute acid stress than the wild type . The G7000 gene was found to be commonly mutated in a laboratory evolution study aimed to increase tolerance to several industrial chemicals. The authors defined YobF as a stress signaling protein . Review:

## Biological Role

Repressed by cyaR (gene.b4438), btsR (protein.P0AFT5), rpoN (protein.P24255). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64508|protein.P64508]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4438|gene.b4438]] `RegulonDB` `S` - regulator=CyaR; target=yobF; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=yobF; function=-
- `represses` <-- [[protein.P24255|protein.P24255]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=yobF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006072,ECOCYC:G7000,GeneID:946338`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1907448-1907591:-; feature_type=gene
