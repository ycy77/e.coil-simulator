---
entity_id: "gene.b0707"
entity_type: "gene"
name: "ybgA"
source_database: "NCBI RefSeq"
source_id: "gene-b0707"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0707"
  - "ybgA"
---

# ybgA

`gene.b0707`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0707`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgA (gene.b0707) is a gene entity. It encodes ybgA (protein.P24252). Encoded protein function: Uncharacterized protein YbgA (ORF169) (TKP) EcoCyc product frame: EG11108-MONOMER. EcoCyc synonyms: tkp. Genomic coordinates: 739001-739510. EcoCyc protein note: No information about this protein was found by a literature search conducted on May 7, 2018.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24252|protein.P24252]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ybgA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002414,ECOCYC:EG11108,GeneID:944853`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:739001-739510:+; feature_type=gene
