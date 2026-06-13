---
entity_id: "reaction.ecocyc.RXN0-722"
entity_type: "reaction"
name: "RXN0-722"
source_database: "EcoCyc"
source_id: "RXN0-722"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-722

`reaction.ecocyc.RXN0-722`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-722`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DUDP + Oxidized-NrdH-Proteins + WATER -> UDP + Reduced-NrdH-Proteins; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: DUDP + Oxidized-NrdH-Proteins + WATER -> UDP + Reduced-NrdH-Proteins; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 2 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX). Substrates: H2O (molecule.C00001), dUDP (molecule.C01346). Products: UDP (molecule.C00015).

## Enriched Pathways

- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

DUDP + Oxidized-NrdH-Proteins + WATER -> UDP + Reduced-NrdH-Proteins; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01346|molecule.C01346]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-722`

## Notes

DUDP + Oxidized-NrdH-Proteins + WATER -> UDP + Reduced-NrdH-Proteins; direction=PHYSIOL-RIGHT-TO-LEFT
