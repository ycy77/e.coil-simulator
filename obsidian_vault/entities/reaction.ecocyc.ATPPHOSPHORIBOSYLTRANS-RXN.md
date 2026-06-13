---
entity_id: "reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN"
entity_type: "reaction"
name: "ATPPHOSPHORIBOSYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "ATPPHOSPHORIBOSYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ATPPHOSPHORIBOSYLTRANS-RXN

`reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ATPPHOSPHORIBOSYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction of histidine biosynthesis EcoCyc reaction equation: PHOSPHORIBOSYL-ATP + PPI -> ATP + PRPP; direction=REVERSIBLE. This is the first reaction of histidine biosynthesis

## Biological Role

Catalyzed by ATP phosphoribosyltransferase (complex.ecocyc.CPLX0-7614). Substrates: Diphosphate (molecule.C00013), 1-(5-Phospho-D-ribosyl)-ATP (molecule.C02739). Products: ATP (molecule.C00002), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This is the first reaction of histidine biosynthesis

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7614|complex.ecocyc.CPLX0-7614]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02739|molecule.C02739]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8179|molecule.ecocyc.CPD-8179]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ATPPHOSPHORIBOSYLTRANS-RXN`

## Notes

PHOSPHORIBOSYL-ATP + PPI -> ATP + PRPP; direction=REVERSIBLE
