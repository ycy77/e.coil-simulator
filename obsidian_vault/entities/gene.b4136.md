---
entity_id: "gene.b4136"
entity_type: "gene"
name: "dsbD"
source_database: "NCBI RefSeq"
source_id: "gene-b4136"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4136"
  - "dsbD"
---

# dsbD

`gene.b4136`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4136`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsbD (gene.b4136) is a gene entity. It encodes dsbD (protein.P36655). Encoded protein function: FUNCTION: Required to facilitate the formation of correct disulfide bonds in some periplasmic proteins and for the assembly of the periplasmic c-type cytochromes. Acts by transferring electrons from cytoplasmic thioredoxin to the periplasm, thereby maintaining the active site of DsbC, DsbE and DsbG in a reduced state. This transfer involves a cascade of disulfide bond formation and reduction steps. EcoCyc product frame: MONOMER0-4573. EcoCyc synonyms: htrI, cutA2, cycZ, dipZ. Genomic coordinates: 4363345-4365042. EcoCyc protein note: Represents the oxidized form of thiol-disulfide exchange protein DsbD EcoCyc protein note: DsbD is an inner membrane protein which acts within a reductive pathway that maintains the periplasmic disulfide oxidoreductases DsbC and DsbG and the cytochrome c maturation protein CcmG in their catalytically active reduced form...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36655|protein.P36655]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013539,ECOCYC:EG12178,GeneID:948649`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4363345-4365042:-; feature_type=gene
