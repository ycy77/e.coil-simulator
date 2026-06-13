---
entity_id: "gene.b3986"
entity_type: "gene"
name: "rplL"
source_database: "NCBI RefSeq"
source_id: "gene-b3986"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3986"
  - "rplL"
---

# rplL

`gene.b3986`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3986`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplL (gene.b3986) is a gene entity. It encodes rplL (protein.P0A7K2). Encoded protein function: FUNCTION: The binding site for several of the GTPase factors involved in protein synthesis (IF-2, EF-Tu, EF-G and RF3). Is thus essential for accurate translation. Deletion of 1 of the L12 dimers from the ribosome (by deleting the binding site on L10) leads to decreased IF-2 association with the 70S ribosome and decreased stimulation of the GTPase activity of EF-G. {ECO:0000269|PubMed:15989950, ECO:0000269|PubMed:22102582}. EcoCyc product frame: MONOMER0-2811. Genomic coordinates: 4180560-4180925. EcoCyc protein note: MONOMER0-2811 is the N-acetylated form of 50S ribosomal subunit protein L12 .

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7K2|protein.P0A7K2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013038,ECOCYC:EG10873,GeneID:948489`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4180560-4180925:+; feature_type=gene
