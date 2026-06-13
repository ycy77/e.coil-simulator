---
entity_id: "gene.b0991"
entity_type: "gene"
name: "ymcE"
source_database: "NCBI RefSeq"
source_id: "gene-b0991"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0991"
  - "ymcE"
---

# ymcE

`gene.b0991`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0991`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymcE (gene.b0991) is a gene entity. It encodes ymcE (protein.P0AAA5). Encoded protein function: Uncharacterized protein YmcE EcoCyc product frame: G6512-MONOMER. Genomic coordinates: 1051847-1052077. EcoCyc protein note: YmcE was mistakenly thought to be a suppressor of fabA6, a temperature-sensitive unsaturated fatty acid auxotroph ; in fact, the suppressor localizes to the gnsA gene, which is located immediately downstream of ymcE . YmcE is also predicted to be the antitoxin of a proposed GnsA-YmcE toxin-antitoxin system . YmcE is predicted to be a bitopic inner membrane protein . Expression of ymcE is increased by cold shock . Overexpression of ymcE increases the tolerance of E. coli to n-butanol .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAA5|protein.P0AAA5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003349,ECOCYC:G6512,GeneID:946951`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1051847-1052077:+; feature_type=gene
