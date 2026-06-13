---
entity_id: "reaction.ecocyc.DCDPKIN-RXN"
entity_type: "reaction"
name: "DCDPKIN-RXN"
source_database: "EcoCyc"
source_id: "DCDPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DCDPKIN-RXN

`reaction.ecocyc.DCDPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DCDPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DCDP + ATP -> DCTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DCDP + ATP -> DCTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX), adk (protein.P69441). Substrates: ATP (molecule.C00002), dCDP (molecule.C00705). Products: ADP (molecule.C00008), dCTP (molecule.C00458).

## Enriched Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

DCDP + ATP -> DCTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00705|molecule.C00705]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DCDPKIN-RXN`

## Notes

DCDP + ATP -> DCTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
