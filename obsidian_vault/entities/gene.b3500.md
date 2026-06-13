---
entity_id: "gene.b3500"
entity_type: "gene"
name: "gor"
source_database: "NCBI RefSeq"
source_id: "gene-b3500"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3500"
  - "gor"
---

# gor

`gene.b3500`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3500`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gor (gene.b3500) is a gene entity. It encodes gor (protein.P06715). Encoded protein function: FUNCTION: Catalyzes the reduction of glutathione disulfide (GSSG) to reduced glutathione (GSH). Constitutes the major mechanism to maintain a high GSH:GSSG ratio in the cytosol. {ECO:0000269|PubMed:6393625}. EcoCyc product frame: GLUTATHIONE-REDUCT-NADPH-MONOMER. EcoCyc synonyms: gorA. Genomic coordinates: 3646299-3647651.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06715|protein.P06715]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gor; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011432,ECOCYC:EG10412,GeneID:948014`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3646299-3647651:+; feature_type=gene
