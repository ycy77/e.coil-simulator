---
entity_id: "gene.b4427"
entity_type: "gene"
name: "micC"
source_database: "NCBI RefSeq"
source_id: "gene-b4427"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4427"
  - "micC"
---

# micC

`gene.b4427`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4427`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

micC (gene.b4427) is a gene entity. EcoCyc product frame: TKE8-RNA. EcoCyc synonyms: IS063, tke8. Genomic coordinates: 1437121-1437231.

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `represses` --> [[gene.b2215|gene.b2215]] `RegulonDB` `S` - regulator=MicC; target=ompC; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=micC; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=micC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0047248,ECOCYC:G0-8901,GeneID:2847713`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1437121-1437231:+; feature_type=gene
