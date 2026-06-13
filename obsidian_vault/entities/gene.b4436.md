---
entity_id: "gene.b4436"
entity_type: "gene"
name: "sibA"
source_database: "NCBI RefSeq"
source_id: "gene-b4436"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4436"
  - "sibA"
---

# sibA

`gene.b4436`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4436`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sibA (gene.b4436) is a gene entity. EcoCyc product frame: RYEC-RNA. EcoCyc synonyms: QUAD1a, tp11, ryeC. Genomic coordinates: 2153311-2153454.

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sibA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=sibA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0047256,ECOCYC:G0-8884,GeneID:2847673`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2153311-2153454:+; feature_type=gene
