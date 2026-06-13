---
entity_id: "protein.P0DPD1"
entity_type: "protein"
name: "ldrC"
source_database: "UniProt"
source_id: "P0DPD1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P0DPD0}; Single-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ldrC b4423 JW5959"
---

# ldrC

`protein.P0DPD1`

## Static

- Type: `protein`
- Source: `UniProt:P0DPD1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P0DPD0}; Single-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Overexpression causes rapid cell killing, probably by disrupting the cell inner membrane and disruption of ATP synthesis. {ECO:0000250|UniProtKB:P0DPD0}. The TAX-83333 genome contains four genes encoding Long Direct Repeat (LDR) peptides - G0-9602, G0-9605, G0-9607, and G0-9041. The first three are clustered together as tandem repeats, while G0-9041 is located elsewhere on the genome. Deletions of ldrABC, ldrD and ldrABDC have no effect under laboratory conditions . Four ldr-like regions, three near ldrD and one near ldrABC, may represent recombination spots for LDRs . All four ldr genes encode small toxic peptides, and each gene is matched with a neighboring rdl gene that encodes an antisense regulatory RNA that is complementary to a region of the ldr gene, forming four Type I toxin-antitoxin (TA) pairs. Type I TA systems consist of a stable toxin-expressing mRNA, which is counteracted by an unstable RNA antitoxin. While many plasmid-encoded TA systems behave as selfish elements and favour their own maintenance at the expense of their host, the role of chromosomally-encoded TA systems is less clear . While ldrC and RNA0-163 "rdlC" are predicted to encode a Type I TA system, no information is available about their function. Related reviews: .

## Annotation

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Overexpression causes rapid cell killing, probably by disrupting the cell inner membrane and disruption of ATP synthesis. {ECO:0000250|UniProtKB:P0DPD0}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4423|gene.b4423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DPD1`
- `KEGG:ecj:JW5959;eco:b4419;eco:b4423;`
- `GeneID:2847775;`
- `GO:GO:0005886`

## Notes

Small toxic polypeptide LdrC
