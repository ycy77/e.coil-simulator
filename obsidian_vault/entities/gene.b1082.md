---
entity_id: "gene.b1082"
entity_type: "gene"
name: "flgK"
source_database: "NCBI RefSeq"
source_id: "gene-b1082"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1082"
  - "flgK"
---

# flgK

`gene.b1082`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1082`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgK (gene.b1082) is a gene entity. It encodes flgK (protein.P33235). Encoded protein function: Flagellar hook-associated protein 1 (HAP1) EcoCyc product frame: EG11967-MONOMER. EcoCyc synonyms: flaS. Genomic coordinates: 1138378-1140021. EcoCyc protein note: Experiments in Salmonella typhimurium using antibodies against the flagellar proteins FlgK and FlgL identify them as junction proteins which connect the filament to the hook . Early studies in E. coli K-12 identified the flaS gene within the region I fla (flagella) genes (see ). For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see . The 'pole-localizer' protein G7087-MONOMER TmaR protects and stabilizes flgK transcripts .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33235|protein.P33235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003660,ECOCYC:EG11967,GeneID:945648`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1138378-1140021:+; feature_type=gene
