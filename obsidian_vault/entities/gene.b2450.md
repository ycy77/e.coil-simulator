---
entity_id: "gene.b2450"
entity_type: "gene"
name: "yffS"
source_database: "NCBI RefSeq"
source_id: "gene-b2450"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2450"
  - "yffS"
---

# yffS

`gene.b2450`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2450`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yffS (gene.b2450) is a gene entity. It encodes yffS (protein.P76550). Encoded protein function: Uncharacterized protein YffS EcoCyc product frame: G7280-MONOMER. Genomic coordinates: 2564523-2565332. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 21, 2016.

## Biological Role

Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76550|protein.P76550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=yffS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008077,ECOCYC:G7280,GeneID:946932`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2564523-2565332:+; feature_type=gene
