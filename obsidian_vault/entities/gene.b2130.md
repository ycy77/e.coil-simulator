---
entity_id: "gene.b2130"
entity_type: "gene"
name: "yehY"
source_database: "NCBI RefSeq"
source_id: "gene-b2130"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2130"
  - "yehY"
---

# yehY

`gene.b2130`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2130`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehY (gene.b2130) is a gene entity. It encodes yehY (protein.P33361). Encoded protein function: FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:26325238}. EcoCyc product frame: YEHY-MONOMER. Genomic coordinates: 2217400-2218557. EcoCyc protein note: YehY is the predicted, integral inner membrane component of a low affinity glycine betaine ABC transporter .

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33361|protein.P33361]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yehY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007038,ECOCYC:EG12011,GeneID:946660`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2217400-2218557:-; feature_type=gene
