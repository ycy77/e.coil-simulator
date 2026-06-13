---
entity_id: "gene.b0821"
entity_type: "gene"
name: "ybiU"
source_database: "NCBI RefSeq"
source_id: "gene-b0821"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0821"
  - "ybiU"
---

# ybiU

`gene.b0821`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0821`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiU (gene.b0821) is a gene entity. It encodes ybiU (protein.P75791). Encoded protein function: Uncharacterized protein YbiU EcoCyc product frame: G6424-MONOMER. Genomic coordinates: 857796-859061. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 23, 2017.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75791|protein.P75791]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=ybiU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002804,ECOCYC:G6424,GeneID:945439`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:857796-859061:-; feature_type=gene
