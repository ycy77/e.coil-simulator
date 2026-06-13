---
entity_id: "gene.b0557"
entity_type: "gene"
name: "borD"
source_database: "NCBI RefSeq"
source_id: "gene-b0557"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0557"
  - "borD"
---

# borD

`gene.b0557`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0557`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

borD (gene.b0557) is a gene entity. It encodes borD (protein.P77330). Encoded protein function: Prophage lipoprotein Bor homolog (Lipoprotein Bor homolog from lambdoid prophage DLP12) EcoCyc product frame: G6312-MONOMER. EcoCyc synonyms: iss, vboR, bor, ybcU. Genomic coordinates: 578600-578893. EcoCyc protein note: BorD is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). BorD is part of the defective prophage DLP12 . borD is expressed under aerobic and anaerobic conditions . borD (vboR) expression responds to the availability of Mg2+ in the external environment and is under the direct control of the PWY0-1458 "PhoPQ two-component system" . bor: blue open reading frame

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0), phoP (protein.P23836), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77330|protein.P77330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=borD; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=borD; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=borD; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001902,ECOCYC:G6312,GeneID:948980`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:578600-578893:-; feature_type=gene
