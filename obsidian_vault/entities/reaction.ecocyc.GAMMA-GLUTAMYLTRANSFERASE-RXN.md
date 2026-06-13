---
entity_id: "reaction.ecocyc.GAMMA-GLUTAMYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "GAMMA-GLUTAMYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "GAMMA-GLUTAMYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GLUTAMYL TRANSPEPTIDASE"
  - "&gamma"
  - "-GLUTAMYLTRANSPEPTIDASE"
---

# GAMMA-GLUTAMYLTRANSFERASE-RXN

`reaction.ecocyc.GAMMA-GLUTAMYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GAMMA-GLUTAMYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

5-L-GLUTAMYL-PEPTIDE + Amino-Acids -> 5-L-GLUTAMYL-AMINO-ACID + Peptides-holder + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-L-GLUTAMYL-PEPTIDE + Amino-Acids -> 5-L-GLUTAMYL-AMINO-ACID + Peptides-holder + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutathione hydrolase (complex.ecocyc.CPLX0-7885). Substrates: a 5-L-glutamyl-[peptide] (molecule.ecocyc.5-L-GLUTAMYL-PEPTIDE), an amino acid (molecule.ecocyc.Amino-Acids). Products: H+ (molecule.C00080), an α-(5-L-glutamyl)-amino acid (molecule.ecocyc.5-L-GLUTAMYL-AMINO-ACID).

## Annotation

5-L-GLUTAMYL-PEPTIDE + Amino-Acids -> 5-L-GLUTAMYL-AMINO-ACID + Peptides-holder + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7885|complex.ecocyc.CPLX0-7885]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-L-GLUTAMYL-AMINO-ACID|molecule.ecocyc.5-L-GLUTAMYL-AMINO-ACID]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.5-L-GLUTAMYL-PEPTIDE|molecule.ecocyc.5-L-GLUTAMYL-PEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Amino-Acids|molecule.ecocyc.Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GAMMA-GLUTAMYLTRANSFERASE-RXN`

## Notes

5-L-GLUTAMYL-PEPTIDE + Amino-Acids -> 5-L-GLUTAMYL-AMINO-ACID + Peptides-holder + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
