---
entity_id: "gene.b3832"
entity_type: "gene"
name: "rmuC"
source_database: "NCBI RefSeq"
source_id: "gene-b3832"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3832"
  - "rmuC"
---

# rmuC

`gene.b3832`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3832`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rmuC (gene.b3832) is a gene entity. It encodes rmuC (protein.P0AG71). Encoded protein function: FUNCTION: Involved in DNA recombination. EcoCyc product frame: EG11472-MONOMER. EcoCyc synonyms: yigN. Genomic coordinates: 4017333-4018760. EcoCyc protein note: RmuC contains a PD-(D/E)XK nuclease domain that is most similar to that of the McrC nuclease . An rmuC mutant generates increased DNA inversions at mini-Tn10 sites in an rmuA mutant background . An rmuC deletion mutant is more sensitive to kasugamycin than wild type . Transcription is induced by nalidixic acid or mitomycin C, and induction requires LexA . RmuC is predicted to be a bitopic inner membrane protein . RmuC: "rearrangement mutator C"

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG71|protein.P0AG71]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012531,ECOCYC:EG11472,GeneID:948966`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4017333-4018760:+; feature_type=gene
