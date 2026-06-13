---
entity_id: "gene.b2536"
entity_type: "gene"
name: "hcaT"
source_database: "NCBI RefSeq"
source_id: "gene-b2536"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2536"
  - "hcaT"
---

# hcaT

`gene.b2536`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2536`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcaT (gene.b2536) is a gene entity. It encodes hcaT (protein.Q47142). Encoded protein function: FUNCTION: Probable permease involved in the uptake of 3-phenylpropionic acid. EcoCyc product frame: HCAT-MONOMER. EcoCyc synonyms: yfhS. Genomic coordinates: 2666707-2667846. EcoCyc protein note: HcaT is a member of the major facilitator superfamily (MFS) of transporters . HcaT is a putative 3-phenylpropionate transporter. The hcaT gene is located immediately downstream of the hcaR gene, whose product regulates expression of the hcaA-D operon responsible for catabolism of 3-phenylpropionic acid . HcaT is predicted to be an inner membrane protein with 12 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47142|protein.Q47142]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008348,ECOCYC:G7330,GeneID:947007`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2666707-2667846:-; feature_type=gene
