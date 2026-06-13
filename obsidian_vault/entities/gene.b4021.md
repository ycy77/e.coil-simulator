---
entity_id: "gene.b4021"
entity_type: "gene"
name: "pepE"
source_database: "NCBI RefSeq"
source_id: "gene-b4021"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4021"
  - "pepE"
---

# pepE

`gene.b4021`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4021`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pepE (gene.b4021) is a gene entity. It encodes pepE (protein.P0A7C6). Encoded protein function: FUNCTION: Hydrolyzes dipeptides containing N-terminal aspartate residues. May play a role in allowing the cell to use peptide aspartate to spare carbon otherwise required for the synthesis of the aspartate family of amino acids. {ECO:0000255|HAMAP-Rule:MF_00510}. EcoCyc product frame: EG11920-MONOMER. Genomic coordinates: 4229453-4230142. EcoCyc protein note: PepE hydrolyzes peptides bond in dipeptides where the first amino acid is aspartate .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7C6|protein.P0A7C6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013146,ECOCYC:EG11920,GeneID:948520`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4229453-4230142:-; feature_type=gene
