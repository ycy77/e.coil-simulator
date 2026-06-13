---
entity_id: "gene.b2621"
entity_type: "gene"
name: "ssrA"
source_database: "NCBI RefSeq"
source_id: "gene-b2621"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2621"
  - "ssrA"
---

# ssrA

`gene.b2621`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2621`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssrA (gene.b2621) is a gene entity. EcoCyc product frame: SSRA-RNA. EcoCyc synonyms: sipB. Genomic coordinates: 2755593-2755955.

## Biological Role

Activated by rpoD (protein.P00579), zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssrA; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=ssrA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008624,ECOCYC:EG30100,GeneID:945053`
- `gbkey:Gene`
- `gene_biotype:other`

## Notes

NC_000913.3:2755593-2755955:+; feature_type=gene
