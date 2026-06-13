---
entity_id: "gene.b2303"
entity_type: "gene"
name: "folX"
source_database: "NCBI RefSeq"
source_id: "gene-b2303"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2303"
  - "folX"
---

# folX

`gene.b2303`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2303`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folX (gene.b2303) is a gene entity. It encodes folX (protein.P0AC19). Encoded protein function: FUNCTION: Catalyzes the epimerization of carbon 2' of the side chain of 7,8-dihydroneopterin triphosphate (H2NTP) to form 7,8-dihydromonapterin triphosphate (H2MTP) (PubMed:9182560, PubMed:9651328). Is required for tetrahydromonapterin biosynthesis, a major pterin in E.coli (PubMed:19897652). {ECO:0000269|PubMed:19897652, ECO:0000269|PubMed:9182560, ECO:0000269|PubMed:9651328}. EcoCyc product frame: H2NTPEPIM-MONOMER. Genomic coordinates: 2421325-2421687.

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC19|protein.P0AC19]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007603,ECOCYC:G7195,GeneID:946781`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2421325-2421687:+; feature_type=gene
