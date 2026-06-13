---
entity_id: "gene.b1340"
entity_type: "gene"
name: "smrA"
source_database: "NCBI RefSeq"
source_id: "gene-b1340"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1340"
  - "smrA"
---

# smrA

`gene.b1340`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1340`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

smrA (gene.b1340) is a gene entity. It encodes smrA (protein.P76053). Encoded protein function: FUNCTION: Has DNA endonuclease activity. Binds DNA. {ECO:0000269|PubMed:21276852}. EcoCyc product frame: G6672-MONOMER. EcoCyc synonyms: ydaL. Genomic coordinates: 1405979-1406542. EcoCyc protein note: SmrA is similar to the Smr domain of MutS2 proteins. The protein binds double-stranded DNA and has endonuclease activity . A crystal structure of the proteolytic fragment containing residues 39-175 of SmrA has been solved at 2.3 Å resolution . smr: small mutS-related (see )

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76053|protein.P76053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004502,ECOCYC:G6672,GeneID:945953`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1405979-1406542:+; feature_type=gene
