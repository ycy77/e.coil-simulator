---
entity_id: "reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN"
entity_type: "reaction"
name: "RIBONUCLEOSIDE-DIP-REDUCTII-RXN"
source_database: "EcoCyc"
source_id: "RIBONUCLEOSIDE-DIP-REDUCTII-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBONUCLEOSIDE-DIP-REDUCTII-RXN

`reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTII-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes deoxynucleoside diphosphates. Reduced glutaredoxin is the reductant. EcoCyc reaction equation: DCDP + Oxidized-NrdH-Proteins + WATER -> CDP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT. This reaction synthesizes deoxynucleoside diphosphates. Reduced glutaredoxin is the reductant.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 2 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX). Substrates: H2O (molecule.C00001), dCDP (molecule.C00705). Products: CDP (molecule.C00112).

## Enriched Pathways

- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

This reaction synthesizes deoxynucleoside diphosphates. Reduced glutaredoxin is the reductant.

## Pathways

- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00705|molecule.C00705]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTII-RXN`

## Notes

DCDP + Oxidized-NrdH-Proteins + WATER -> CDP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT
