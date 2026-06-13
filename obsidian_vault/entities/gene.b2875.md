---
entity_id: "gene.b2875"
entity_type: "gene"
name: "yqeB"
source_database: "NCBI RefSeq"
source_id: "gene-b2875"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2875"
  - "yqeB"
---

# yqeB

`gene.b2875`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2875`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqeB (gene.b2875) is a gene entity. It encodes yqeB (protein.Q46808). Encoded protein function: Uncharacterized protein YqeB EcoCyc product frame: G7494-MONOMER. Genomic coordinates: 3012614-3014239. EcoCyc protein note: Partial phylogenetic profiling suggested that yqeB belongs to a system connected to selenium-dependent molybdenum hydroxylases .

## Biological Role

Repressed by nac (protein.Q47005). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46808|protein.Q46808]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yqeB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009441,ECOCYC:G7494,GeneID:947357`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3012614-3014239:-; feature_type=gene
