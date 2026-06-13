---
entity_id: "gene.b0901"
entity_type: "gene"
name: "ycaK"
source_database: "NCBI RefSeq"
source_id: "gene-b0901"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0901"
  - "ycaK"
---

# ycaK

`gene.b0901`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0901`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaK (gene.b0901) is a gene entity. It encodes ycaK (protein.P43340). Encoded protein function: Uncharacterized NAD(P)H oxidoreductase YcaK (EC 1.6.99.-) EcoCyc product frame: EG12702-MONOMER. Genomic coordinates: 949668-950258. EcoCyc protein note: Based on sequence similarity, YcaK was predicted to be an NAD(P)H dehydrogenase . YcaK has been predicted to be an electron transfer flavoprotein-NAD/FAD/quinone oxidoreductase .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43340|protein.P43340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ycaK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003065,ECOCYC:EG12702,GeneID:945520`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:949668-950258:+; feature_type=gene
