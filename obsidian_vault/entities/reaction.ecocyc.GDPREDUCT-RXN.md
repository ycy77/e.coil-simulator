---
entity_id: "reaction.ecocyc.GDPREDUCT-RXN"
entity_type: "reaction"
name: "GDPREDUCT-RXN"
source_database: "EcoCyc"
source_id: "GDPREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GDPREDUCT-RXN

`reaction.ecocyc.GDPREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GDPREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Necessary for DNA synthesis. EcoCyc reaction equation: DGDP + Ox-Thioredoxin + WATER -> GDP + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT. Necessary for DNA synthesis.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 1 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX). Substrates: H2O (molecule.C00001), dGDP (molecule.C00361). Products: GDP (molecule.C00035).

## Enriched Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

Necessary for DNA synthesis.

## Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00361|molecule.C00361]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GDPREDUCT-RXN`

## Notes

DGDP + Ox-Thioredoxin + WATER -> GDP + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT
