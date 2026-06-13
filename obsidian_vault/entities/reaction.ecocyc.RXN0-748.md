---
entity_id: "reaction.ecocyc.RXN0-748"
entity_type: "reaction"
name: "RXN0-748"
source_database: "EcoCyc"
source_id: "RXN0-748"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-748

`reaction.ecocyc.RXN0-748`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-748`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DGDP + Oxidized-NrdH-Proteins + WATER -> GDP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT EcoCyc reaction equation: DGDP + Oxidized-NrdH-Proteins + WATER -> GDP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 2 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX). Substrates: H2O (molecule.C00001), dGDP (molecule.C00361). Products: GDP (molecule.C00035).

## Enriched Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

DGDP + Oxidized-NrdH-Proteins + WATER -> GDP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00361|molecule.C00361]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-748`

## Notes

DGDP + Oxidized-NrdH-Proteins + WATER -> GDP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT
