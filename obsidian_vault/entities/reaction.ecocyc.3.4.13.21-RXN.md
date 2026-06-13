---
entity_id: "reaction.ecocyc.3.4.13.21-RXN"
entity_type: "reaction"
name: "3.4.13.21-RXN"
source_database: "EcoCyc"
source_id: "3.4.13.21-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PepE gene product (Salmonella typhimurium)"
  - "Peptidase E"
  - "Aspartyl dipeptidase"
---

# 3.4.13.21-RXN

`reaction.ecocyc.3.4.13.21-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.13.21-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond in a dipeptide where the first amino acid is aspartate. EcoCyc reaction equation: Dipeptides-With-Asp-At-N-Terminal + WATER -> L-ASPARTATE + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond in a dipeptide where the first amino acid is aspartate.

## Biological Role

Catalyzed by pepE (protein.P0A7C6). Substrates: H2O (molecule.C00001), a dipetide with an N-terminal L-aspartate (molecule.ecocyc.Dipeptides-With-Asp-At-N-Terminal). Products: L-Aspartate (molecule.C00049), a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

This reaction is the hydrolysis of a peptide bond in a dipeptide where the first amino acid is aspartate.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7C6|protein.P0A7C6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Dipeptides-With-Asp-At-N-Terminal|molecule.ecocyc.Dipeptides-With-Asp-At-N-Terminal]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.13.21-RXN`

## Notes

Dipeptides-With-Asp-At-N-Terminal + WATER -> L-ASPARTATE + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT
