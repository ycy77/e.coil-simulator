---
entity_id: "gene.b0551"
entity_type: "gene"
name: "quuD"
source_database: "NCBI RefSeq"
source_id: "gene-b0551"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0551"
  - "quuD"
---

# quuD

`gene.b0551`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0551`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

quuD (gene.b0551) is a gene entity. It encodes quuD (protein.Q47274). Encoded protein function: FUNCTION: Positively regulate expression of some phage genes. Bacterial host RNA polymerase modified by antitermination proteins transcribes through termination sites that otherwise prevent expression of the regulated genes (By similarity). {ECO:0000250}. EcoCyc product frame: G6307-MONOMER. EcoCyc synonyms: ybcQ. Genomic coordinates: 573956-574339. EcoCyc protein note: QuuD is similar to the bacteriophage 21 Q protein, a transcriptional antiterminator . Overexpression of QuuD leads to increased expression of the essD transcription unit, which encodes the DLP12 prophage lysis cassette . A quuD deletion mutant shows reduced biofilm formation and curli production .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47274|protein.Q47274]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001883,ECOCYC:G6307,GeneID:945177`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:573956-574339:+; feature_type=gene
