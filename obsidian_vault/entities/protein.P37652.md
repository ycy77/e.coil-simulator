---
entity_id: "protein.P37652"
entity_type: "protein"
name: "bcsB"
source_database: "UniProt"
source_id: "P37652"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type I membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bcsB yhjN b3532 JW3500"
---

# bcsB

`protein.P37652`

## Static

- Type: `protein`
- Source: `UniProt:P37652`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type I membrane protein.

## Enriched Summary

FUNCTION: Binds the cellulose synthase activator, bis-(3'-5') cyclic diguanylic acid (c-di-GMP). {ECO:0000250}. BcsB is encoded in a predicted operon together with bcsA, bcsZ and bcsC. In other organisms, these genes are involved in cellulose biosynthesis, a characteristic of the rdar (red, dry and rough) morphotype. However, the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110-derivative strain produces cellulose and has dramatically altered biofilm morphology . In the cellulose-producing strain E. coli 1094, the inner membrane and cytosolic Bcs proteins - BcsA, BcsB, BscQ, BcsG, BcsE, BcsR and BcsF - organize in a multisubunit, stable macrocomplex; two-hybrid assays identified multiple direct interactions between the subunits and a low resolution structure has been obtained (see also ). E. coli 1094 with ΔbcsB mutation displays a defect in cellulose biosynthesis . Overexpression of bcsB (in the K-12 strains BW25113 and MG1655) induces cell flocculation and enhances biofilm formation...

## Biological Role

Component of cellulose synthase (complex.ecocyc.CPLX0-8125).

## Annotation

FUNCTION: Binds the cellulose synthase activator, bis-(3'-5') cyclic diguanylic acid (c-di-GMP). {ECO:0000250}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8125|complex.ecocyc.CPLX0-8125]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3532|gene.b3532]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37652`
- `KEGG:ecj:JW3500;eco:b3532;ecoc:C3026_19135;`
- `GeneID:948045;`
- `GO:GO:0005886; GO:0006011; GO:0030244`

## Notes

Cyclic di-GMP-binding protein (Cellulose synthase regulatory subunit)
