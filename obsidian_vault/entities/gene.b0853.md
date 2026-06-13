---
entity_id: "gene.b0853"
entity_type: "gene"
name: "ybjN"
source_database: "NCBI RefSeq"
source_id: "gene-b0853"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0853"
  - "ybjN"
---

# ybjN

`gene.b0853`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0853`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjN (gene.b0853) is a gene entity. It encodes ybjN (protein.P0AAY6). Encoded protein function: Uncharacterized protein YbjN EcoCyc product frame: G6447-MONOMER. Genomic coordinates: 892957-893433. EcoCyc protein note: Both overexpression and mutation of YbjN has pleiotropic effects in the cell involving the production of flagella and fimbriae and acid resistance . Using a "fuzzy functional form" alignment mechanism, YbjN was predicted to have thiol-disulfide oxidoreductase activity . It was initially found that overexpression of YbjN suppresses the temperature-sensitive growth defect of several coaA alleles as well as the ilu-1 allele . The authors hypothesized that YbjN functions to generally stabilize unstable proteins . Overexpression of ybjN leads to a growth defect in liquid media, decreased expression of fimbriae, decreased acid resistance, and induction of many stress response genes. A ybjN mutant has increased flagellar motility and appears to overproduce colanic acid, leading to a mucoid appearance . ybjN insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A ybjN deletion mutant has a modest decrease in IR survival . Expression of ybjN is growth stage- and temperature-dependent .

## Biological Role

Repressed by lrp (protein.P0ACJ0), oxyR (protein.P0ACQ4). Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAY6|protein.P0AAY6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=ybjN; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=ybjN; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=ybjN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002910,ECOCYC:G6447,GeneID:945482`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:892957-893433:+; feature_type=gene
