---
entity_id: "gene.b3637"
entity_type: "gene"
name: "rpmB"
source_database: "NCBI RefSeq"
source_id: "gene-b3637"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3637"
  - "rpmB"
---

# rpmB

`gene.b3637`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3637`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmB (gene.b3637) is a gene entity. It encodes rpmB (protein.P0A7M2). Encoded protein function: Large ribosomal subunit protein bL28 (50S ribosomal protein L28) EcoCyc product frame: EG10886-MONOMER. Genomic coordinates: 3811438-3811674. EcoCyc protein note: The L28 protein is a component of the 50S subunit of the ribosome and is required for ribosome assembly . L28 interacts with 23S rRNA and crosslinks to L9 . L15 and L17 stimulate the interaction of L28 with 23S rRNA . L28 is phosphorylated at Thr8 . L28 is labeled by the macrolides carbomycin A, niddamycin and tylosin, which inhibit ribosomal activity . Expression of rpmBG is under ppGpp/DksA-dependent negative stringent control during amino acid starvation .

## Biological Role

Repressed by yfeC (protein.P0AD37).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7M2|protein.P0A7M2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AD37|protein.P0AD37]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011885,ECOCYC:EG10886,GeneID:946941`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3811438-3811674:-; feature_type=gene
