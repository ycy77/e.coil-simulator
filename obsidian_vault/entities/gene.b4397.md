---
entity_id: "gene.b4397"
entity_type: "gene"
name: "creA"
source_database: "NCBI RefSeq"
source_id: "gene-b4397"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4397"
  - "creA"
---

# creA

`gene.b4397`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4397`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

creA (gene.b4397) is a gene entity. It encodes creA (protein.P0AE91). Encoded protein function: Protein CreA (Catabolite regulation protein A) EcoCyc product frame: EG11217-MONOMER. EcoCyc synonyms: yjjD. Genomic coordinates: 4635521-4635994. EcoCyc protein note: Deletion of creA causes a slight increase in the expression of a creD-lacZ transcriptional fusion during aerobic growth on pyruvate minimal medium and a decrease in creD-lacZ expression during anaerobic growth on glucose minimal medium compared to wild-type .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE91|protein.P0AE91]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=creA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014426,ECOCYC:EG11217,GeneID:948920`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4635521-4635994:+; feature_type=gene
