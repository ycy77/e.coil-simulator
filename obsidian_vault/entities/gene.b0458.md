---
entity_id: "gene.b0458"
entity_type: "gene"
name: "ylaC"
source_database: "NCBI RefSeq"
source_id: "gene-b0458"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0458"
  - "ylaC"
---

# ylaC

`gene.b0458`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0458`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ylaC (gene.b0458) is a gene entity. It encodes ylaC (protein.P0AAS0). Encoded protein function: Inner membrane protein YlaC EcoCyc product frame: G6253-MONOMER. Genomic coordinates: 478781-479251. EcoCyc protein note: YlaC is an inner membrane protein with two predicted transmembrane domains. The C-terminus is located in the cytoplasm . A knockout mutant of this gene was sensitive to boric acid exposure; a complementation assay restored its intrinsic boric acid resistance. Double and triple knockout mutants (ΔEG12760ΔylaC, ΔylaCΔgarPΔG7261 and ΔylaCΔgarPΔG6994) exhibited increasing sensitivity, respectively .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAS0|protein.P0AAS0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001587,ECOCYC:G6253,GeneID:948876`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:478781-479251:-; feature_type=gene
