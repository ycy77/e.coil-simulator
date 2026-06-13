---
entity_id: "gene.b2670"
entity_type: "gene"
name: "alaE"
source_database: "NCBI RefSeq"
source_id: "gene-b2670"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2670"
  - "alaE"
---

# alaE

`gene.b2670`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2670`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alaE (gene.b2670) is a gene entity. It encodes alaE (protein.P64550). Encoded protein function: FUNCTION: Exports L-alanine. {ECO:0000255|HAMAP-Rule:MF_00914, ECO:0000269|PubMed:21531828}. EcoCyc product frame: G7399-MONOMER. EcoCyc synonyms: ygaW. Genomic coordinates: 2799164-2799613.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64550|protein.P64550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=alaE; function=-+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=alaE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=alaE; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008793,ECOCYC:G7399,GeneID:947147`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2799164-2799613:+; feature_type=gene
