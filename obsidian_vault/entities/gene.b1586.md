---
entity_id: "gene.b1586"
entity_type: "gene"
name: "ynfD"
source_database: "NCBI RefSeq"
source_id: "gene-b1586"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1586"
  - "ynfD"
---

# ynfD

`gene.b1586`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1586`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfD (gene.b1586) is a gene entity. It encodes ynfD (protein.P76172). Encoded protein function: Uncharacterized protein YnfD EcoCyc product frame: G6844-MONOMER. Genomic coordinates: 1657565-1657870. EcoCyc protein note: YnfD has a signal peptide that is cleaved from the mature protein. Similarity of YnfD to proteins in other organisms is discussed .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76172|protein.P76172]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynfD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005297,ECOCYC:G6844,GeneID:946133`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1657565-1657870:+; feature_type=gene
