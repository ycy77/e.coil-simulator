---
entity_id: "reaction.ecocyc.DTDPKIN-RXN"
entity_type: "reaction"
name: "DTDPKIN-RXN"
source_database: "EcoCyc"
source_id: "DTDPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DTDPKIN-RXN

`reaction.ecocyc.DTDPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DTDPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TDP + ATP -> TTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TDP + ATP -> TTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX), adk (protein.P69441). Substrates: ATP (molecule.C00002), dTDP (molecule.C00363). Products: ADP (molecule.C00008), dTTP (molecule.C00459).

## Enriched Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

TDP + ATP -> TTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00363|molecule.C00363]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DTDPKIN-RXN`

## Notes

TDP + ATP -> TTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
