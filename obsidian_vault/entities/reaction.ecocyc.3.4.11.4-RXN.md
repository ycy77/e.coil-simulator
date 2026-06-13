---
entity_id: "reaction.ecocyc.3.4.11.4-RXN"
entity_type: "reaction"
name: "3.4.11.4-RXN"
source_database: "EcoCyc"
source_id: "3.4.11.4-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Tripeptidase"
  - "Aminotripeptidase"
  - "Aminoexotripeptidase"
  - "Lymphopeptidase"
  - "Imidoendopeptidase"
  - "Peptidase B"
---

# 3.4.11.4-RXN

`reaction.ecocyc.3.4.11.4-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.11.4-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond between the most first and second residues in a tripeptide. It can cleave peptides beginning with leucine, lysine, methionine and phenylalanine, including x-glycine-glycine, x-glycine-x and x-leucine-glycine. It cannot cleave dipeptides or tetrapeptides. EcoCyc reaction equation: TRIPEPTIDES + WATER -> DIPEPTIDES + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond between the most first and second residues in a tripeptide. It can cleave peptides beginning with leucine, lysine, methionine and phenylalanine, including x-glycine-glycine, x-glycine-x and x-leucine-glycine. It cannot cleave dipeptides or tetrapeptides.

## Biological Role

Catalyzed by peptidase T (complex.ecocyc.CPLX0-3041). Substrates: H2O (molecule.C00001), a tripeptide (molecule.ecocyc.TRIPEPTIDES). Products: a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20), a dipeptide (molecule.ecocyc.DIPEPTIDES).

## Annotation

This reaction is the hydrolysis of a peptide bond between the most first and second residues in a tripeptide. It can cleave peptides beginning with leucine, lysine, methionine and phenylalanine, including x-glycine-glycine, x-glycine-x and x-leucine-glycine. It cannot cleave dipeptides or tetrapeptides.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3041|complex.ecocyc.CPLX0-3041]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DIPEPTIDES|molecule.ecocyc.DIPEPTIDES]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TRIPEPTIDES|molecule.ecocyc.TRIPEPTIDES]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.11.4-RXN`

## Notes

TRIPEPTIDES + WATER -> DIPEPTIDES + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT
