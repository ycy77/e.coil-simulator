---
entity_id: "gene.b3290"
entity_type: "gene"
name: "trkA"
source_database: "NCBI RefSeq"
source_id: "gene-b3290"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3290"
  - "trkA"
---

# trkA

`gene.b3290`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3290`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trkA (gene.b3290) is a gene entity. It encodes trkA (protein.P0AGI8). Encoded protein function: FUNCTION: Part of the constitutive potassium transport systems TrkG and TrkH. May regulate the transport activity of TrkG and TrkH systems. Binds to NAD(+) and NADH. {ECO:0000269|PubMed:2674131, ECO:0000269|PubMed:8412700}. EcoCyc product frame: TRKA-MONOMER. Genomic coordinates: 3436518-3437894. EcoCyc protein note: Early studies in E. coli K-12 identified four separate K+ uptake systems: two constitutive systems [TrkA (also called Trk) and TrkD (also called Kup)], a high affinity system (Kdp) and a non-saturable system TrkF (see also . Although initially thought to be a single system TrkA/Trk activity was later shown to result from the activity of two low affinity, high rate K+ transporters (TRKG-MONOMER "TrkG" and TRKH-MONOMER "TrkH") which function in conjunction with TRKA-MONOMER "TrkA", a peripheral membrane protein that binds NAD+ and is essential for TrkG/H activity . TrkA is a peripheral membrane protein that is loosely bound to the cytoplasmic side of the inner membrane; when over-produced, TrkA is present mainly in the soluble fraction; no membrane bound TrkA is detected in EG12304 "trkE", trkG or trkH mutant strains indicating that the products of these genes are required for the normal membrane association of TrkA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGI8|protein.P0AGI8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010787,ECOCYC:EG11019,GeneID:947788`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3436518-3437894:+; feature_type=gene
