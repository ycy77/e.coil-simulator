---
entity_id: "gene.b4453"
entity_type: "gene"
name: "ldrD"
source_database: "NCBI RefSeq"
source_id: "gene-b4453"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4453"
  - "ldrD"
---

# ldrD

`gene.b4453`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4453`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldrD (gene.b4453) is a gene entity. It encodes ldrD (protein.Q6BF25). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Overexpression causes rapid cell killing and nucleoid condensation of the host cell (PubMed:12123448). Overexpression induces stress-response and a number of membrane protein genes. May inhibit ATP synthesis due to its insertion in the cell inner membrane (By similarity). {ECO:0000250|UniProtKB:P0DPD0, ECO:0000269|PubMed:12123448, ECO:0000269|PubMed:18710431}. EcoCyc product frame: MONOMER0-921. Genomic coordinates: 3699980-3700087. EcoCyc protein note: The TAX-83333 genome contains four genes encoding Long Direct Repeat (LDR) peptides - G0-9602, G0-9605, G0-9607, and G0-9041. The first three are clustered together as tandem repeats, while G0-9041 is located elsewhere on the genome. Deletions of ldrABC, ldrD and ldrABDC have no effect under laboratory conditions . Four ldr-like regions, three near ldrD and one near ldrABC, may represent recombination spots for LDRs . All four ldr genes encode small toxic peptides, and each gene is matched with a neighboring rdl gene that encodes an antisense regulatory RNA that is complementary to a region of the ldr gene, forming four Type I toxin-antitoxin (TA) pairs. Type I TA systems consist of a stable toxin-expressing mRNA, which is counteracted by an unstable RNA antitoxin...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q6BF25|protein.Q6BF25]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047284,ECOCYC:G0-9041,GeneID:2847730`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3699980-3700087:-; feature_type=gene
