---
entity_id: "gene.b4419"
entity_type: "gene"
name: "ldrA"
source_database: "NCBI RefSeq"
source_id: "gene-b4419"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4419"
  - "ldrA"
---

# ldrA

`gene.b4419`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4419`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldrA (gene.b4419) is a gene entity. It encodes ldrA (protein.P0DPD0). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Inhibits ATP synthesis possibly due to its insertion in the cell inner membrane, ATP levels drop over 50% 2 minutes after induction (PubMed:24513967). Overexpression is toxic leading to cell death, it inhibits cell growth within 30 minutes; C-terminally tagged versions of the protein are toxic while N-terminally tagged versions are not (PubMed:24513967). {ECO:0000269|PubMed:24513967}. EcoCyc product frame: MONOMER0-1601. Genomic coordinates: 1269168-1269275. EcoCyc protein note: The TAX-83333 genome contains four genes encoding Long Direct Repeat (LDR) peptides - G0-9602, G0-9605, G0-9607, and G0-9041. The first three are clustered together as tandem repeats, while G0-9041 is located elsewhere on the genome. Deletions of ldrABC, ldrD and ldrABDC have no effect under laboratory conditions . Four ldr-like regions, three near ldrD and one near ldrABC, may represent recombination spots for LDRs . All four ldr genes encode small toxic peptides, and each gene is matched with a neighboring rdl gene that encodes an antisense regulatory RNA that is complementary to a region of the ldr gene, forming four Type I toxin-antitoxin (TA) pairs...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPD0|protein.P0DPD0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047280,ECOCYC:G0-9602,GeneID:2847733`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1269168-1269275:-; feature_type=gene
