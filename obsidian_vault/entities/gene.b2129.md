---
entity_id: "gene.b2129"
entity_type: "gene"
name: "yehX"
source_database: "NCBI RefSeq"
source_id: "gene-b2129"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2129"
  - "yehX"
---

# yehX

`gene.b2129`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2129`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehX (gene.b2129) is a gene entity. It encodes yehX (protein.P33360). Encoded protein function: FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:26325238}. EcoCyc product frame: YEHX-MONOMER. Genomic coordinates: 2216481-2217407. EcoCyc protein note: YehX is the predicted, ATP binding component of a low affinity glycine betaine ABC transporter .

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33360|protein.P33360]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yehX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007034,ECOCYC:EG12010,GeneID:946659`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2216481-2217407:-; feature_type=gene
