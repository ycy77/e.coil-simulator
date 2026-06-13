---
entity_id: "gene.b1929"
entity_type: "gene"
name: "yedE"
source_database: "NCBI RefSeq"
source_id: "gene-b1929"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1929"
  - "yedE"
---

# yedE

`gene.b1929`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1929`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yedE (gene.b1929) is a gene entity. It encodes yedE (protein.P31064). Encoded protein function: Probable transporter YedE EcoCyc product frame: EG11660-MONOMER. Genomic coordinates: 2008277-2009482. EcoCyc protein note: YedE is predicted to be an inner membrane protein containing ten transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . Comparative genomics implicates yedE in selenium transport . E. coli YedE is a member of the YedE/YeeE (YeeE) family of uncharacterized transporters . yedE is downregulated under multiple stress conditions (heat, cold, oxidative stress, and antibiotic treatment) .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31064|protein.P31064]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006422,ECOCYC:EG11660,GeneID:945192`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2008277-2009482:+; feature_type=gene
