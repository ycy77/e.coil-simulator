---
entity_id: "gene.b2086"
entity_type: "gene"
name: "yegS"
source_database: "NCBI RefSeq"
source_id: "gene-b2086"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2086"
  - "yegS"
---

# yegS

`gene.b2086`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2086`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegS (gene.b2086) is a gene entity. It encodes yegS (protein.P76407). Encoded protein function: FUNCTION: In vitro phosphorylates phosphatidylglycerol but not diacylglycerol; the in vivo substrate is unknown. EcoCyc product frame: G7123-MONOMER. Genomic coordinates: 2168712-2169611. EcoCyc protein note: YegS is a lipid kinase with phosphatidylglycerol kinase activity in vitro . It shows sequence similarity to a family of eukaryotic non-protein kinases . The physiological role of YegS is unknown, but a possible role in the response to acid stress has been proposed . A crystal structure of YegS has been determined at 1.9 Å resolution; the protein shows structural similarity to a family of NAD kinases . In an experimental evolution experiment for growth under glucose limitation in a chemostat, inactivation of yegS conferred an increase in fitness .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76407|protein.P76407]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006911,ECOCYC:G7123,GeneID:946626`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2168712-2169611:+; feature_type=gene
