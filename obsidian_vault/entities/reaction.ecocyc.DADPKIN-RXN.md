---
entity_id: "reaction.ecocyc.DADPKIN-RXN"
entity_type: "reaction"
name: "DADPKIN-RXN"
source_database: "EcoCyc"
source_id: "DADPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DADPKIN-RXN

`reaction.ecocyc.DADPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DADPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DADP + ATP -> DATP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DADP + ATP -> DATP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX). Substrates: ATP (molecule.C00002), dADP (molecule.C00206). Products: ADP (molecule.C00008), dATP (molecule.C00131).

## Enriched Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

DADP + ATP -> DATP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00206|molecule.C00206]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DADPKIN-RXN`

## Notes

DADP + ATP -> DATP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
