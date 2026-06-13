---
entity_id: "gene.b1098"
entity_type: "gene"
name: "tmk"
source_database: "NCBI RefSeq"
source_id: "gene-b1098"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1098"
  - "tmk"
---

# tmk

`gene.b1098`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1098`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tmk (gene.b1098) is a gene entity. It encodes tmk (protein.P0A720). Encoded protein function: FUNCTION: Catalyzes the reversible phosphorylation of deoxythymidine monophosphate (dTMP) to deoxythymidine diphosphate (dTDP), using ATP as its preferred phosphoryl donor (PubMed:8631667). Situated at the junction of both de novo and salvage pathways of deoxythymidine triphosphate (dTTP) synthesis, is essential for DNA synthesis and cellular growth. {ECO:0000269|PubMed:8631667}. EcoCyc product frame: DTMPKI-MONOMER. EcoCyc synonyms: ycfG. Genomic coordinates: 1155124-1155765.

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A720|protein.P0A720]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003714,ECOCYC:EG12302,GeneID:945663`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1155124-1155765:+; feature_type=gene
