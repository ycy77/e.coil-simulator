---
entity_id: "gene.b1196"
entity_type: "gene"
name: "ycgY"
source_database: "NCBI RefSeq"
source_id: "gene-b1196"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1196"
  - "ycgY"
---

# ycgY

`gene.b1196`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1196`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgY (gene.b1196) is a gene entity. It encodes ycgY (protein.P76012). Encoded protein function: Uncharacterized protein YcgY EcoCyc product frame: G6625-MONOMER. Genomic coordinates: 1245160-1245600. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 12, 2017.

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76012|protein.P76012]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycgY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004019,ECOCYC:G6625,GeneID:945761`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1245160-1245600:+; feature_type=gene
