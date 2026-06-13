---
entity_id: "gene.b0857"
entity_type: "gene"
name: "potI"
source_database: "NCBI RefSeq"
source_id: "gene-b0857"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0857"
  - "potI"
---

# potI

`gene.b0857`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0857`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potI (gene.b0857) is a gene entity. It encodes potI (protein.P0AFL1). Encoded protein function: FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for the translocation of the substrate across the membrane (Probable). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000305}. EcoCyc product frame: POTI-MONOMER. Genomic coordinates: 897084-897929. EcoCyc protein note: potI encodes one of two integral membrane subunits of an ATP-dependent putrescine uptake system; PotI is predicted to contain 6 transmembrane regions; PotI has 37% sequence similarity with PotC - the integral membrane subunit of the spermidine ABC transporter PotABCD

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFL1|protein.P0AFL1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002919,ECOCYC:EG11632,GeneID:945485`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:897084-897929:+; feature_type=gene
