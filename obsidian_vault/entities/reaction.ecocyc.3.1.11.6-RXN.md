---
entity_id: "reaction.ecocyc.3.1.11.6-RXN"
entity_type: "reaction"
name: "3.1.11.6-RXN"
source_database: "EcoCyc"
source_id: "3.1.11.6-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Exonuclease VII"
  - "E.coli exonuclease VII"
---

# 3.1.11.6-RXN

`reaction.ecocyc.3.1.11.6-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.11.6-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Single-Stranded-DNAs + WATER -> Ribonucleoside-Monophosphates + SS-Oligodeoxyribonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Single-Stranded-DNAs + WATER -> Ribonucleoside-Monophosphates + SS-Oligodeoxyribonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by exodeoxyribonuclease VII (complex.ecocyc.CPLX-3946), recJ (protein.P21893). Substrates: H2O (molecule.C00001). Products: a ribonucleoside 5'-monophosphate (molecule.ecocyc.Ribonucleoside-Monophosphates), a single-stranded oligodeoxyribonucleotide (molecule.ecocyc.SS-Oligodeoxyribonucleotides).

## Annotation

Single-Stranded-DNAs + WATER -> Ribonucleoside-Monophosphates + SS-Oligodeoxyribonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-3946|complex.ecocyc.CPLX-3946]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P21893|protein.P21893]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Ribonucleoside-Monophosphates|molecule.ecocyc.Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SS-Oligodeoxyribonucleotides|molecule.ecocyc.SS-Oligodeoxyribonucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.11.6-RXN`

## Notes

Single-Stranded-DNAs + WATER -> Ribonucleoside-Monophosphates + SS-Oligodeoxyribonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT
