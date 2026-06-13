---
entity_id: "gene.b2274"
entity_type: "gene"
name: "yfbO"
source_database: "NCBI RefSeq"
source_id: "gene-b2274"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2274"
  - "yfbO"
---

# yfbO

`gene.b2274`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2274`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfbO (gene.b2274) is a gene entity. It encodes yfbO (protein.P76485). Encoded protein function: Uncharacterized protein YfbO EcoCyc product frame: G7181-MONOMER. Genomic coordinates: 2388635-2389057. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 16, 2018.

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76485|protein.P76485]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfbO; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007518,ECOCYC:G7181,GeneID:946752`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2388635-2389057:+; feature_type=gene
