---
entity_id: "gene.b1376"
entity_type: "gene"
name: "uspF"
source_database: "NCBI RefSeq"
source_id: "gene-b1376"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1376"
  - "uspF"
---

# uspF

`gene.b1376`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1376`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uspF (gene.b1376) is a gene entity. It encodes uspF (protein.P37903). Encoded protein function: Universal stress protein F EcoCyc product frame: G6699-MONOMER. EcoCyc synonyms: yzzL, ynaF, UP03. Genomic coordinates: 1435185-1435619. EcoCyc protein note: UspF is a nucleotide binding protein that belongs to the class II (UspF/G) subfamily of universal stress proteins . Based on sequence similarity, UspF is expected to dimerize and to have an ATP-binding site like that of the Methanococcus jannaschii MJ0577 protein . UspF promotes adhesion at the expense of motility. Single deletions of uspF or uspG have a negative effect on fimbria-dependent adhesion and show enhanced motility. However, the uspFG double mutant shows no adhesion phenotype. A uspF uspG double mutant is more sensitive to oxidative stress and the antibiotic streptonigrin . UspF is upregulated under glucose-limited fed-batch conditions . Transcription of uspF in stationary phase is increased in a pgi mutant compared to wild type . Abundance of UspG is increased in response to nitrosative stress . Review:

## Biological Role

Activated by yeiE (protein.P0ACR4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37903|protein.P37903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004605,ECOCYC:G6699,GeneID:945948`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1435185-1435619:-; feature_type=gene
