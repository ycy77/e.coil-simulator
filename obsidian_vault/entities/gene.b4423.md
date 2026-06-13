---
entity_id: "gene.b4423"
entity_type: "gene"
name: "ldrC"
source_database: "NCBI RefSeq"
source_id: "gene-b4423"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4423"
  - "ldrC"
---

# ldrC

`gene.b4423`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4423`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldrC (gene.b4423) is a gene entity. It encodes ldrC (protein.P0DPD1). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Overexpression causes rapid cell killing, probably by disrupting the cell inner membrane and disruption of ATP synthesis. {ECO:0000250|UniProtKB:P0DPD0}. EcoCyc product frame: MONOMER0-1603. Genomic coordinates: 1270238-1270345. EcoCyc protein note: The TAX-83333 genome contains four genes encoding Long Direct Repeat (LDR) peptides - G0-9602, G0-9605, G0-9607, and G0-9041. The first three are clustered together as tandem repeats, while G0-9041 is located elsewhere on the genome. Deletions of ldrABC, ldrD and ldrABDC have no effect under laboratory conditions . Four ldr-like regions, three near ldrD and one near ldrABC, may represent recombination spots for LDRs . All four ldr genes encode small toxic peptides, and each gene is matched with a neighboring rdl gene that encodes an antisense regulatory RNA that is complementary to a region of the ldr gene, forming four Type I toxin-antitoxin (TA) pairs. Type I TA systems consist of a stable toxin-expressing mRNA, which is counteracted by an unstable RNA antitoxin. While many plasmid-encoded TA systems behave as selfish elements and favour their own maintenance at the expense of their host, the role of chromosomally-encoded TA systems is less clear...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPD1|protein.P0DPD1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047282,ECOCYC:G0-9607,GeneID:2847775`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1270238-1270345:-; feature_type=gene
