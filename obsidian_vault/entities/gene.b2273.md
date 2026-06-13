---
entity_id: "gene.b2273"
entity_type: "gene"
name: "yfbN"
source_database: "NCBI RefSeq"
source_id: "gene-b2273"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2273"
  - "yfbN"
---

# yfbN

`gene.b2273`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2273`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfbN (gene.b2273) is a gene entity. It encodes yfbN (protein.P76484). Encoded protein function: Uncharacterized protein YfbN EcoCyc product frame: G7180-MONOMER. Genomic coordinates: 2387710-2388426. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 16, 2018.

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76484|protein.P76484]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfbN; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007511,ECOCYC:G7180,GeneID:946748`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2387710-2388426:-; feature_type=gene
