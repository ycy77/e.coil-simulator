---
entity_id: "gene.b3655"
entity_type: "gene"
name: "yicH"
source_database: "NCBI RefSeq"
source_id: "gene-b3655"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3655"
  - "yicH"
---

# yicH

`gene.b3655`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3655`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yicH (gene.b3655) is a gene entity. It encodes yicH (protein.P31433). Encoded protein function: AsmA family protein YicH EcoCyc product frame: EG11684-MONOMER. Genomic coordinates: 3830457-3832166. EcoCyc protein note: Sequence similarity suggests that YicH may containe β-barrel structure(s) . YicH is predicted to be a bitopic inner membrane protein . YicH, G7875-MONOMER TamB, G7690-MONOMER YhdP, G6703-MONOMER YdbH, and EG12251-MONOMER YhjG are EG11361-MONOMER AsmA-like paralogs predicted to contain an N-terminal inner membrane anchor and a large periplasmic region with chorein-N and AsmA-like domains .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31433|protein.P31433]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011949,ECOCYC:EG11684,GeneID:948171`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3830457-3832166:+; feature_type=gene
