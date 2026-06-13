---
entity_id: "protein.P0DPD0"
entity_type: "protein"
name: "ldrA"
source_database: "UniProt"
source_id: "P0DPD0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:24513967}; Single-pass membrane protein {ECO:0000305|PubMed:24513967}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ldrA b4419 JW5957"
---

# ldrA

`protein.P0DPD0`

## Static

- Type: `protein`
- Source: `UniProt:P0DPD0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:24513967}; Single-pass membrane protein {ECO:0000305|PubMed:24513967}.

## Enriched Summary

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Inhibits ATP synthesis possibly due to its insertion in the cell inner membrane, ATP levels drop over 50% 2 minutes after induction (PubMed:24513967). Overexpression is toxic leading to cell death, it inhibits cell growth within 30 minutes; C-terminally tagged versions of the protein are toxic while N-terminally tagged versions are not (PubMed:24513967). {ECO:0000269|PubMed:24513967}. The TAX-83333 genome contains four genes encoding Long Direct Repeat (LDR) peptides - G0-9602, G0-9605, G0-9607, and G0-9041. The first three are clustered together as tandem repeats, while G0-9041 is located elsewhere on the genome. Deletions of ldrABC, ldrD and ldrABDC have no effect under laboratory conditions . Four ldr-like regions, three near ldrD and one near ldrABC, may represent recombination spots for LDRs . All four ldr genes encode small toxic peptides, and each gene is matched with a neighboring rdl gene that encodes an antisense regulatory RNA that is complementary to a region of the ldr gene, forming four Type I toxin-antitoxin (TA) pairs. Type I TA systems consist of a stable toxin-expressing mRNA, which is counteracted by an unstable RNA antitoxin...

## Annotation

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Inhibits ATP synthesis possibly due to its insertion in the cell inner membrane, ATP levels drop over 50% 2 minutes after induction (PubMed:24513967). Overexpression is toxic leading to cell death, it inhibits cell growth within 30 minutes; C-terminally tagged versions of the protein are toxic while N-terminally tagged versions are not (PubMed:24513967). {ECO:0000269|PubMed:24513967}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4419|gene.b4419]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DPD0`
- `KEGG:ecj:JW5957;eco:b4419;eco:b4423;`
- `GeneID:2847733;`
- `GO:GO:0005886`

## Notes

Small toxic polypeptide LdrA
