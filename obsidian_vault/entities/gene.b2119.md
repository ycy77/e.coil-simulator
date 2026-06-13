---
entity_id: "gene.b2119"
entity_type: "gene"
name: "yehL"
source_database: "NCBI RefSeq"
source_id: "gene-b2119"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2119"
  - "yehL"
---

# yehL

`gene.b2119`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2119`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehL (gene.b2119) is a gene entity. It encodes yehL (protein.P33348). Encoded protein function: Uncharacterized protein YehL EcoCyc product frame: EG11998-MONOMER. Genomic coordinates: 2204596-2205684. EcoCyc protein note: YehL defines a subfamily of the MoxR AAA+ ("ATPases associated with various cellular activities") family . Its limited phylogenetic distribution suggests a highly specialized role .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33348|protein.P33348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yehL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007006,ECOCYC:EG11998,GeneID:946656`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2204596-2205684:+; feature_type=gene
