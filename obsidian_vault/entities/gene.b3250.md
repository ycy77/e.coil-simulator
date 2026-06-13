---
entity_id: "gene.b3250"
entity_type: "gene"
name: "mreC"
source_database: "NCBI RefSeq"
source_id: "gene-b3250"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3250"
  - "mreC"
---

# mreC

`gene.b3250`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3250`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mreC (gene.b3250) is a gene entity. It encodes mreC (protein.P16926). Encoded protein function: FUNCTION: Involved in formation and maintenance of cell shape. Responsible for formation of rod shape. May also contribute to regulation of formation of penicillin-binding proteins. {ECO:0000269|PubMed:15612918, ECO:0000269|PubMed:2687239}. EcoCyc product frame: EG10609-MONOMER. Genomic coordinates: 3398875-3399978.

## Biological Role

Repressed by bolA (protein.P0ABE2), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16926|protein.P16926]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ABE2|protein.P0ABE2]] `RegulonDB` `S` - regulator=BolA; target=mreC; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mreC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010658,ECOCYC:EG10609,GeneID:947655`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3398875-3399978:-; feature_type=gene
