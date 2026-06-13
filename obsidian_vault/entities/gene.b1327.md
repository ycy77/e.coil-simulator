---
entity_id: "gene.b1327"
entity_type: "gene"
name: "ycjY"
source_database: "NCBI RefSeq"
source_id: "gene-b1327"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1327"
  - "ycjY"
---

# ycjY

`gene.b1327`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1327`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjY (gene.b1327) is a gene entity. It encodes ycjY (protein.P76049). Encoded protein function: Uncharacterized protein YcjY EcoCyc product frame: G6663-MONOMER. Genomic coordinates: 1390933-1391853. EcoCyc protein note: Overexpression of YcjY from a plasmid causes a filamentous phenotype . ycjY expression was increased during growth under nitrogen starvation conditions .

## Biological Role

Repressed by pgrR (protein.P77333).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76049|protein.P76049]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=ycjY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004453,ECOCYC:G6663,GeneID:945988`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1390933-1391853:-; feature_type=gene
