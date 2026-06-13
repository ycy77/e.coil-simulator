---
entity_id: "gene.b1764"
entity_type: "gene"
name: "selD"
source_database: "NCBI RefSeq"
source_id: "gene-b1764"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1764"
  - "selD"
---

# selD

`gene.b1764`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1764`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

selD (gene.b1764) is a gene entity. It encodes selD (protein.P16456). Encoded protein function: FUNCTION: Synthesizes selenophosphate from selenide and ATP. {ECO:0000255|HAMAP-Rule:MF_00625, ECO:0000269|PubMed:22081394, ECO:0000269|PubMed:2405383}. EcoCyc product frame: EG10943-MONOMER. EcoCyc synonyms: fdhB. Genomic coordinates: 1846965-1848008.

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16456|protein.P16456]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005872,ECOCYC:EG10943,GeneID:946768`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1846965-1848008:-; feature_type=gene
