---
entity_id: "gene.b1273"
entity_type: "gene"
name: "yciN"
source_database: "NCBI RefSeq"
source_id: "gene-b1273"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1273"
  - "yciN"
---

# yciN

`gene.b1273`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1273`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciN (gene.b1273) is a gene entity. It encodes yciN (protein.P0AB61). Encoded protein function: Protein YciN EcoCyc product frame: EG12868-MONOMER. Genomic coordinates: 1330417-1330668. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 10, 2008.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB61|protein.P0AB61]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yciN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004269,ECOCYC:EG12868,GeneID:945860`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1330417-1330668:-; feature_type=gene
