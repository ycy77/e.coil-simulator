---
entity_id: "gene.b0643"
entity_type: "gene"
name: "ybeL"
source_database: "NCBI RefSeq"
source_id: "gene-b0643"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0643"
  - "ybeL"
---

# ybeL

`gene.b0643`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0643`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeL (gene.b0643) is a gene entity. It encodes ybeL (protein.P0AAT9). Encoded protein function: Uncharacterized protein YbeL EcoCyc product frame: EG12851-MONOMER. Genomic coordinates: 675018-675500. EcoCyc protein note: YbeL is subject to C-terminal tagging with the SsrA degradation signal while the ribosome stalls at the stop codon . The C-terminal proline residue and the preceding glutamate residue were identified as determinants for efficient SsrA tagging . A peptide consisting of the N-terminal 120 amino acids of YbeL has been used as a translational fusion tag as well as in a transcriptional fusion strategy to facilitate overexpression and purification of properly folded membrane proteins.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAT9|protein.P0AAT9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002199,ECOCYC:EG12851,GeneID:945252`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:675018-675500:+; feature_type=gene
