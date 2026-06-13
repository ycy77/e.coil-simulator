---
entity_id: "gene.b0577"
entity_type: "gene"
name: "ybdG"
source_database: "NCBI RefSeq"
source_id: "gene-b0577"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0577"
  - "ybdG"
---

# ybdG

`gene.b0577`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0577`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdG (gene.b0577) is a gene entity. It encodes ybdG (protein.P0AAT4). Encoded protein function: FUNCTION: Functions as a component of a mechanosensing system that transmits signals triggered by external osmotic changes to intracellular factors (PubMed:31256002). Probably plays a crucial role in cellular protection against high osmotic pressure (PubMed:31256002). Also confers protection against mild hypoosmotic shock (PubMed:20616037). Overexpression confers protection against severe shocks (PubMed:20616037). Lacks measurable transport activity (PubMed:20616037, PubMed:31256002). {ECO:0000269|PubMed:20616037, ECO:0000269|PubMed:31256002}. EcoCyc product frame: G6323-MONOMER. EcoCyc synonyms: mscM. Genomic coordinates: 603416-604663.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAT4|protein.P0AAT4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001978,ECOCYC:G6323,GeneID:946243`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:603416-604663:-; feature_type=gene
