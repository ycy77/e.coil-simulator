---
entity_id: "gene.b3720"
entity_type: "gene"
name: "bglH"
source_database: "NCBI RefSeq"
source_id: "gene-b3720"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3720"
  - "bglH"
---

# bglH

`gene.b3720`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3720`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bglH (gene.b3720) is a gene entity. It encodes bglH (protein.P26218). Encoded protein function: FUNCTION: Part of a cryptic operon that is poorly expressed in vivo. May be an ancestral sugar porin with a broad carbohydrate specificity; it binds aromatic beta-D-glucosides such as arbutin and salicin, but with low affinity compared to the binding of maltooligosaccharides to the LamB porin. EcoCyc product frame: EG11364-MONOMER. EcoCyc synonyms: yieC. Genomic coordinates: 3900604-3902220. EcoCyc protein note: BglH is an outer-membrane porin coded for by a gene in the cryptic bgl operon. When expressed, it forms a slightly voltage-dependent membrane channel that weakly binds carbohydrates. Its greatest binding affinity is for β-glucosides .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26218|protein.P26218]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bglH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012165,ECOCYC:EG11364,GeneID:948228`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3900604-3902220:-; feature_type=gene
