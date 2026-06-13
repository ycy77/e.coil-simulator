---
entity_id: "reaction.ecocyc.UDPREDUCT-RXN"
entity_type: "reaction"
name: "UDPREDUCT-RXN"
source_database: "EcoCyc"
source_id: "UDPREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPREDUCT-RXN

`reaction.ecocyc.UDPREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Necessary for DNA synthesis. EcoCyc reaction equation: DUDP + Ox-Thioredoxin + WATER -> UDP + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT. Necessary for DNA synthesis.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 1 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX). Substrates: H2O (molecule.C00001), dUDP (molecule.C01346). Products: UDP (molecule.C00015).

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
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01346|molecule.C01346]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UDPREDUCT-RXN`

## Notes

DUDP + Ox-Thioredoxin + WATER -> UDP + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT
