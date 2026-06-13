---
entity_id: "gene.b2848"
entity_type: "gene"
name: "yqeJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2848"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2848"
  - "yqeJ"
---

# yqeJ

`gene.b2848`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2848`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqeJ (gene.b2848) is a gene entity. It encodes yqeJ (protein.Q46943). Encoded protein function: Uncharacterized protein YqeJ EcoCyc product frame: G7468-MONOMER. Genomic coordinates: 2989304-2989786. EcoCyc protein note: yqeJ is located within a remnant of an ETT2 (type III secretion system) pathogenicity island that is fully present in pathogenic strains such as E. coli O157:H7 and at least partially present in most sequenced E. coli and Shigella strains . ETT2 has been shown to contribute to pathogenesis .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46943|protein.Q46943]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yqeJ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009354,ECOCYC:G7468,GeneID:947328`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2989304-2989786:+; feature_type=gene
