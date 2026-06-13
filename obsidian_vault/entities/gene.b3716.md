---
entity_id: "gene.b3716"
entity_type: "gene"
name: "cbrB"
source_database: "NCBI RefSeq"
source_id: "gene-b3716"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3716"
  - "cbrB"
---

# cbrB

`gene.b3716`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3716`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbrB (gene.b3716) is a gene entity. It encodes cbrB (protein.P31468). Encoded protein function: Inner membrane protein CbrB (CreB-regulated gene B protein) EcoCyc product frame: EG11726-MONOMER. EcoCyc synonyms: yieI. Genomic coordinates: 3897506-3897973. EcoCyc protein note: Transcription of cbrB, the first gene of the predicted cbrBC transcription unit, is induced by the CreBC two-component system by minimal media growth conditions . Certain cbrBC mutants show hypersensitivity to nitrofurzone . CbrB is an inner membrane protein with four predicted transmembrane domains. The C terminus is located in the cytoplasm . CbrB: "creB-regulated"

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31468|protein.P31468]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cbrB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012156,ECOCYC:EG11726,GeneID:948231`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3897506-3897973:+; feature_type=gene
