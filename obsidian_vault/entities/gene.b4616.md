---
entity_id: "gene.b4616"
entity_type: "gene"
name: "istR"
source_database: "NCBI RefSeq"
source_id: "gene-b4616"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4616"
  - "istR"
---

# istR

`gene.b4616`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4616`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

istR (gene.b4616) is a gene entity. EcoCyc product frame: RNA0-282. EcoCyc synonyms: psrA19, istR-1, istR-2. Genomic coordinates: 3853118-3853257.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `represses` --> [[gene.b4618|gene.b4618]] `RegulonDB` `S` - regulator=IstR-1; target=tisB; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=istR; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10201,GeneID:5061525`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3853118-3853257:-; feature_type=gene
