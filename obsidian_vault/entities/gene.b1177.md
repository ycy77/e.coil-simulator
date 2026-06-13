---
entity_id: "gene.b1177"
entity_type: "gene"
name: "ycgJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1177"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1177"
  - "ycgJ"
---

# ycgJ

`gene.b1177`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1177`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgJ (gene.b1177) is a gene entity. It encodes ycgJ (protein.P76001). Encoded protein function: Uncharacterized protein YcgJ EcoCyc product frame: G6614-MONOMER. Genomic coordinates: 1226600-1226968. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2020.

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76001|protein.P76001]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycgJ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ycgJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003946,ECOCYC:G6614,GeneID:946155`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1226600-1226968:+; feature_type=gene
