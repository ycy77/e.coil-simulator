---
entity_id: "gene.b2270"
entity_type: "gene"
name: "yfbK"
source_database: "NCBI RefSeq"
source_id: "gene-b2270"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2270"
  - "yfbK"
---

# yfbK

`gene.b2270`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2270`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfbK (gene.b2270) is a gene entity. It encodes yfbK (protein.P76481). Encoded protein function: Uncharacterized protein YfbK EcoCyc product frame: G7177-MONOMER. Genomic coordinates: 2383995-2385722. EcoCyc protein note: Proteomic analysis demonstrated that YfbK is resistant to ionic detergents and contains protein motifs typical for amyloid-forming proteins . While wild-type E. coli shows significantly decreased swarming motility upon exposure to volatile organic compounds (VOCs) produced by Bacillus subtilis, a yfbK null mutant shows no significant difference in swarming motility upon VOC treatment .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76481|protein.P76481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yfbK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007501,ECOCYC:G7177,GeneID:946743`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2383995-2385722:-; feature_type=gene
