---
entity_id: "gene.b1969"
entity_type: "gene"
name: "hprR"
source_database: "NCBI RefSeq"
source_id: "gene-b1969"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1969"
  - "hprR"
---

# hprR

`gene.b1969`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1969`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hprR (gene.b1969) is a gene entity. It encodes hprR (protein.P76340). Encoded protein function: FUNCTION: Member of a two-component regulatory system HprR/HprS involved in response to hydrogen peroxide (PubMed:25568260, PubMed:27983483). Regulates the expression of at least 5 operons, cyoABCDE, hprRS, hiuH, cusRS and cusCFBA. Bifunctional regulator that acts as an activator and a repressor (PubMed:25568260). {ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}. EcoCyc product frame: MONOMER0-4341. EcoCyc synonyms: yedW. Genomic coordinates: 2038152-2038823. EcoCyc protein note: Based on Genomic SELEX screening, the two-component system (TCS) HprSR (previously called YedVW) has been characterized, and five operons, cyoABCDE, yedVW, hiuH, cusSR, and cusCFBA, were predicted to be under the direct control of this TCS; however, its regulatory role has only been examined for the hiuH gene . On the other hand, Shimada et al. reported, also based on Genomic SELEX screening, that HrpR binds strongly only between the TU0-1822 and TU0-1821 operons and that with minor strength HprR binds between TU0-13468 and hprR genes; these authors classified this protein as a single-target transcription factor . Genome-wide HprR binding sites were also determined in vivo by chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium...

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76340|protein.P76340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hprR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006533,ECOCYC:G7057,GeneID:946486`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2038152-2038823:-; feature_type=gene
