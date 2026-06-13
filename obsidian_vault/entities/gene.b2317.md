---
entity_id: "gene.b2317"
entity_type: "gene"
name: "dedA"
source_database: "NCBI RefSeq"
source_id: "gene-b2317"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2317"
  - "dedA"
---

# dedA

`gene.b2317`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2317`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dedA (gene.b2317) is a gene entity. It encodes dedA (protein.P0ABP6). Encoded protein function: FUNCTION: Could be involved in undecaprenyl phosphate (UndP) transport and recycling (PubMed:36450357). When expressed in B.subtilis uptA-ykoX double mutant, confers high-level resistance to the amphomycin derivative MX2401, which binds UndP in the outer leaflet of the cytoplasmic membrane and prevents its transport across the membrane and its recycling (PubMed:36450357). {ECO:0000269|PubMed:36450357}. EcoCyc product frame: EG10216-MONOMER. Genomic coordinates: 2434082-2434741. EcoCyc protein note: DedA is predicted to be an inner membrane protein with four transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . DedA is a member of the DedA family of proteins . E. coli K-12 contains 7 other DedA family members, namely G7609-MONOMER "YqjA", EG11824 "YghB", EG11571 "YabI", EG12017 "YohD", G7407 "YqaA", G6945-MONOMER "YdjX" and G6947 "YdjZ". Collectively, the DedA family is essential in E. coli K-12 . DedA: "downstream E. coli DNA (from hisT)"

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABP6|protein.P0ABP6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007653,ECOCYC:EG10216,GeneID:946798`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2434082-2434741:-; feature_type=gene
