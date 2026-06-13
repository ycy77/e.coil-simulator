---
entity_id: "reaction.ecocyc.CDPREDUCT-RXN"
entity_type: "reaction"
name: "CDPREDUCT-RXN"
source_database: "EcoCyc"
source_id: "CDPREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CDPREDUCT-RXN

`reaction.ecocyc.CDPREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CDPREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Necessary for DNA synthesis. EcoCyc reaction equation: DCDP + Ox-Thioredoxin + WATER -> CDP + Red-Thioredoxin; direction=RIGHT-TO-LEFT. Necessary for DNA synthesis.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 1 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX). Substrates: H2O (molecule.C00001), dCDP (molecule.C00705). Products: CDP (molecule.C00112).

## Enriched Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

Necessary for DNA synthesis.

## Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00705|molecule.C00705]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CDPREDUCT-RXN`

## Notes

DCDP + Ox-Thioredoxin + WATER -> CDP + Red-Thioredoxin; direction=RIGHT-TO-LEFT
