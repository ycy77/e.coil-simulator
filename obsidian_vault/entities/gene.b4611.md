---
entity_id: "gene.b4611"
entity_type: "gene"
name: "sibE"
source_database: "NCBI RefSeq"
source_id: "gene-b4611"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4611"
  - "sibE"
---

# sibE

`gene.b4611`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4611`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sibE (gene.b4611) is a gene entity. EcoCyc product frame: RNA0-332. EcoCyc synonyms: QUAD1e, rygE. Genomic coordinates: 3195097-3195240.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sibE; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=sibE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:G0-10602,GeneID:5061520`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3195097-3195240:-; feature_type=gene
