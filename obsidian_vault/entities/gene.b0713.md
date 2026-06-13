---
entity_id: "gene.b0713"
entity_type: "gene"
name: "pxpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0713"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0713"
  - "pxpA"
---

# pxpA

`gene.b0713`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0713`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pxpA (gene.b0713) is a gene entity. It encodes pxpA (protein.P75746). Encoded protein function: FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000255|HAMAP-Rule:MF_00691, ECO:0000269|PubMed:28830929}. EcoCyc product frame: G6382-MONOMER. EcoCyc synonyms: ybgL. Genomic coordinates: 745165-745899. EcoCyc protein note: Overexpression of pxpBCA leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpA deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . While wild-type E. coli shows significantly decreased swarming motility upon exposure to volatile organic compounds (VOCs) produced by Bacillus subtilis, a pxpA null mutant shows no significant difference in swarming motility upon VOC treatment . PxpA: "prokaryotic 5-oxoprolinase A"

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75746|protein.P75746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002431,ECOCYC:G6382,GeneID:945318`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:745165-745899:+; feature_type=gene
