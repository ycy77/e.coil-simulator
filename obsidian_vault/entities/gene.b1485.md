---
entity_id: "gene.b1485"
entity_type: "gene"
name: "ddpC"
source_database: "NCBI RefSeq"
source_id: "gene-b1485"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1485"
  - "ddpC"
---

# ddpC

`gene.b1485`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1485`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddpC (gene.b1485) is a gene entity. It encodes ddpC (protein.P77463). Encoded protein function: FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: YDDQ-MONOMER. EcoCyc synonyms: yddQ. Genomic coordinates: 1559014-1559910. EcoCyc protein note: DdpC is one of two predicted inner membrane subunits of a putative ATP-dependent D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . DdpC is predicted to be an inner membrane protein with 5 or 6 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . ddp: D,D-dipeptide

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77463|protein.P77463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ddpC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004953,ECOCYC:G6779,GeneID:946028`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1559014-1559910:-; feature_type=gene
