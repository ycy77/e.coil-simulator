---
entity_id: "gene.b0885"
entity_type: "gene"
name: "aat"
source_database: "NCBI RefSeq"
source_id: "gene-b0885"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0885"
  - "aat"
---

# aat

`gene.b0885`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0885`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aat (gene.b0885) is a gene entity. It encodes aat (protein.P0A8P1). Encoded protein function: FUNCTION: Functions in the N-end rule pathway of protein degradation where it conjugates Leu, Phe and, less efficiently, Met from aminoacyl-tRNAs to the N-termini of proteins containing an N-terminal arginine or lysine. EcoCyc product frame: EG11112-MONOMER. EcoCyc synonyms: ycaA. Genomic coordinates: 926728-927432. EcoCyc protein note: L/F-transferase (Aat) attaches leucine and phenylalanine to exposed amino-terminal arginines and lysines on proteins. This is a key step in the ClpAP-dependent N-end rule degradation pathway. L/F-transferase catalyzes the transfer of leucine and phenylalanine from charged tRNA to amino-terminal lysines and arginines on substrate proteins . When assayed with small peptides, Aat only modifies peptides bearing amino-terminal L-arginine and L-lysine, although the simple dipeptide D-lysyl-D-valine is not a substrate . Testing with purified Aat and actual protein substrates shows that Aat will only transfer to amino-terminal, rather than internal, arginines in proteins . Though addition of both leucine and phenylalanine occurs in vitro, an in vivo experiment with arginine-β-galactosidase yielded only leucine addition . In one case, purified L/F-transferase has been shown to transfer methionine onto the amino-terminus of substrate peptides...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8P1|protein.P0A8P1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003009,ECOCYC:EG11112,GeneID:945490`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:926728-927432:-; feature_type=gene
