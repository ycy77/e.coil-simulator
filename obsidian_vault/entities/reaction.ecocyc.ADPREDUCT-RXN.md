---
entity_id: "reaction.ecocyc.ADPREDUCT-RXN"
entity_type: "reaction"
name: "ADP reductase"
source_database: "EcoCyc"
source_id: "ADPREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADP reductase

`reaction.ecocyc.ADPREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADPREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Necessary for DNA synthesis. EcoCyc reaction equation: DADP + Ox-Thioredoxin + WATER -> ADP + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT. Necessary for DNA synthesis.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 1 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX). Substrates: H2O (molecule.C00001), dADP (molecule.C00206). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

Necessary for DNA synthesis.

## Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00206|molecule.C00206]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ADPREDUCT-RXN`

## Notes

DADP + Ox-Thioredoxin + WATER -> ADP + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT
