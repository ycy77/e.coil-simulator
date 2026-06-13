---
entity_id: "gene.b4080"
entity_type: "gene"
name: "mdtP"
source_database: "NCBI RefSeq"
source_id: "gene-b4080"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4080"
  - "mdtP"
---

# mdtP

`gene.b4080`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4080`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtP (gene.b4080) is a gene entity. It encodes mdtP (protein.P32714). Encoded protein function: FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride. {ECO:0000269|PubMed:11257026}. EcoCyc product frame: EG11952-MONOMER. EcoCyc synonyms: yjcP, sdsP. Genomic coordinates: 4299564-4301030. EcoCyc protein note: mdtP encodes a putative multidrug resistance protein; MdtP from E. coli K-12 W3110 has 26% sequence identity and 47% similarity (over 466 residues) with OprM - the Pseudomonas aeruginosa outer membrane component of the MexAB multidrug resistance pump; deletion of mdtP from strain W3110 results in increased susceptibility to acriflavin, puromycin and tetraphenylarsonium chloride . MdtP is the outer membrane component of a putative efflux pump implicated in resistance to sulfonamide antibiotics . sdsP: sulfa drug sensitivity mdtP: multi drug transporter

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32714|protein.P32714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013366,ECOCYC:EG11952,GeneID:948583`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4299564-4301030:-; feature_type=gene
