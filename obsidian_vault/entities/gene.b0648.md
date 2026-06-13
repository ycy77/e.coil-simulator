---
entity_id: "gene.b0648"
entity_type: "gene"
name: "ybeU"
source_database: "NCBI RefSeq"
source_id: "gene-b0648"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0648"
  - "ybeU"
---

# ybeU

`gene.b0648`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0648`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeU (gene.b0648) is a gene entity. It encodes ybeU (protein.P77427). Encoded protein function: Uncharacterized protein YbeU EcoCyc product frame: G6355-MONOMER. Genomic coordinates: 679508-680215. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 13, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77427|protein.P77427]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybeU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002220,ECOCYC:G6355,GeneID:945244`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:679508-680215:+; feature_type=gene
