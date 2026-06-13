---
entity_id: "gene.b0804"
entity_type: "gene"
name: "ybiX"
source_database: "NCBI RefSeq"
source_id: "gene-b0804"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0804"
  - "ybiX"
---

# ybiX

`gene.b0804`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0804`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiX (gene.b0804) is a gene entity. It encodes ybiX (protein.P75779). Encoded protein function: PKHD-type hydroxylase YbiX (EC 1.14.11.-) EcoCyc product frame: G6413-MONOMER. Genomic coordinates: 838530-839207. EcoCyc protein note: Expression of ybiX is induced in Fe2+ chelator and fur mutant strains . A candidate FUR-box is located upstream to the fiuA gene in E. coli; fiuA and ybiX may form an operon .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9). Activated by yieP (protein.P31475).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75779|protein.P75779]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P31475|protein.P31475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ybiX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002746,ECOCYC:G6413,GeneID:947502`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:838530-839207:-; feature_type=gene
