---
entity_id: "gene.b4067"
entity_type: "gene"
name: "actP"
source_database: "NCBI RefSeq"
source_id: "gene-b4067"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4067"
  - "actP"
---

# actP

`gene.b4067`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4067`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

actP (gene.b4067) is a gene entity. It encodes actP (protein.P32705). Encoded protein function: FUNCTION: Transports acetate. Also able to transport glycolate. {ECO:0000269|PubMed:14563880}. EcoCyc product frame: YJCG-MONOMER. EcoCyc synonyms: yjcG. Genomic coordinates: 4283253-4284902.

## Biological Role

Repressed by fis (protein.P0A6R3), rob (protein.P0ACI0). Activated by crp (protein.P0ACJ8), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32705|protein.P32705]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=actP; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=actP; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=actP; function=-
- `represses` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013328,ECOCYC:EG11942,GeneID:948575`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4283253-4284902:-; feature_type=gene
