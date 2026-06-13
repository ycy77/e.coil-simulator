---
entity_id: "gene.b0964"
entity_type: "gene"
name: "csgI"
source_database: "NCBI RefSeq"
source_id: "gene-b0964"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0964"
  - "csgI"
---

# csgI

`gene.b0964`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0964`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgI (gene.b0964) is a gene entity. It encodes yccT (protein.P0A8X4). Encoded protein function: UPF0319 protein YccT EcoCyc product frame: G6498-MONOMER. EcoCyc synonyms: yccT. Genomic coordinates: 1027111-1027773. EcoCyc protein note: Expression of csgI (formerly yccT) is activated by the biofilm regulator CsgD . CsgI is implicated in the inhibition of curli fimbriae formation; CsgI is detected in the periplasmic space (in a CsgD-overexpressing strain) . csgI: curli synthesis inhibitor

## Biological Role

Repressed by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), glaR (protein.P37338). Activated by csgD (protein.P52106).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8X4|protein.P0A8X4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgI; function=+
- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=csgI; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003262,ECOCYC:G6498,GeneID:945577`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1027111-1027773:-; feature_type=gene
