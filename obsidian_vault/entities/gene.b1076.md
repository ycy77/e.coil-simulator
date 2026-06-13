---
entity_id: "gene.b1076"
entity_type: "gene"
name: "flgE"
source_database: "NCBI RefSeq"
source_id: "gene-b1076"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1076"
  - "flgE"
---

# flgE

`gene.b1076`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1076`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgE (gene.b1076) is a gene entity. It encodes flgE (protein.P75937). Encoded protein function: Flagellar hook protein FlgE EcoCyc product frame: G361-MONOMER. EcoCyc synonyms: flaK. Genomic coordinates: 1132574-1133782. EcoCyc protein note: FlgE is the basic subunit that polymerizes to form the flexible hook structure which couples the envelope-embedded flagellar rotary motor to the rigid flagellar filament in Escherichia coli. Early studies in E. coli K-12 identified the flaK gene within the region I fla (flagella) genes (see ). For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see . flgE exhibits mosaic evolution patterns in E. coli .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75937|protein.P75937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003647,ECOCYC:G361,GeneID:945636`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1132574-1133782:+; feature_type=gene
