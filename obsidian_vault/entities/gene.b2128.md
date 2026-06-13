---
entity_id: "gene.b2128"
entity_type: "gene"
name: "yehW"
source_database: "NCBI RefSeq"
source_id: "gene-b2128"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2128"
  - "yehW"
---

# yehW

`gene.b2128`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2128`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehW (gene.b2128) is a gene entity. It encodes yehW (protein.P33359). Encoded protein function: FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:26325238}. EcoCyc product frame: YEHW-MONOMER. Genomic coordinates: 2215745-2216476. EcoCyc protein note: YehW is the predicted, integral inner membrane component of a low affinity glycine betaine ABC transporter .

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33359|protein.P33359]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yehW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007032,ECOCYC:EG12009,GeneID:949028`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2215745-2216476:-; feature_type=gene
