---
entity_id: "gene.b1441"
entity_type: "gene"
name: "ydcT"
source_database: "NCBI RefSeq"
source_id: "gene-b1441"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1441"
  - "ydcT"
---

# ydcT

`gene.b1441`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1441`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcT (gene.b1441) is a gene entity. It encodes ydcT (protein.P77795). Encoded protein function: FUNCTION: Probably part of the ABC transporter complex YdcSTUV. Probably responsible for energy coupling to the transport system. {ECO:0000305}. EcoCyc product frame: YDCT-MONOMER. Genomic coordinates: 1512817-1513830. EcoCyc protein note: YdcT is the predicted ATP-binding component of an uncharacterized ABC transporter .

## Biological Role

Repressed by yeiE (protein.P0ACR4). Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77795|protein.P77795]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ydcT; function=+
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004805,ECOCYC:G6752,GeneID:946007`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1512817-1513830:+; feature_type=gene
