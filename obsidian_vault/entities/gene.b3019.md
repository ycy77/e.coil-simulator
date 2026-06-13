---
entity_id: "gene.b3019"
entity_type: "gene"
name: "parC"
source_database: "NCBI RefSeq"
source_id: "gene-b3019"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3019"
  - "parC"
---

# parC

`gene.b3019`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3019`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

parC (gene.b3019) is a gene entity. It encodes parC (protein.P0AFI2). Encoded protein function: FUNCTION: Topoisomerase IV is essential for chromosome segregation; it is the principal protein responsible for decatenating newly replicated chromosomes (PubMed:9334322). It relaxes supercoiled DNA (PubMed:12269820, PubMed:16023670, PubMed:21300644). MukB stimulates the relaxation activity of topoisomerase IV and also has a modest effect on decatenation (PubMed:20921377). {ECO:0000269|PubMed:12269820, ECO:0000269|PubMed:16023670, ECO:0000269|PubMed:20921377, ECO:0000269|PubMed:21300644, ECO:0000269|PubMed:9334322}. EcoCyc product frame: EG10686-MONOMER. Genomic coordinates: 3163715-3165973. EcoCyc protein note: The purified ParC protein is a dimer in solution .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFI2|protein.P0AFI2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009916,ECOCYC:EG10686,GeneID:947499`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3163715-3165973:-; feature_type=gene
