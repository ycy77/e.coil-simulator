---
entity_id: "reaction.ecocyc.RXN0-747"
entity_type: "reaction"
name: "RXN0-747"
source_database: "EcoCyc"
source_id: "RXN0-747"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-747

`reaction.ecocyc.RXN0-747`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-747`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DADP + Oxidized-NrdH-Proteins + WATER -> ADP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT EcoCyc reaction equation: DADP + Oxidized-NrdH-Proteins + WATER -> ADP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ribonucleoside-diphosphate reductase 2 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX). Substrates: H2O (molecule.C00001), dADP (molecule.C00206). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

DADP + Oxidized-NrdH-Proteins + WATER -> ADP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00206|molecule.C00206]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-747`

## Notes

DADP + Oxidized-NrdH-Proteins + WATER -> ADP + Reduced-NrdH-Proteins; direction=RIGHT-TO-LEFT
