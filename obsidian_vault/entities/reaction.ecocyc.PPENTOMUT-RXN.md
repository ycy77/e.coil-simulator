---
entity_id: "reaction.ecocyc.PPENTOMUT-RXN"
entity_type: "reaction"
name: "PPENTOMUT-RXN"
source_database: "EcoCyc"
source_id: "PPENTOMUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PPENTOMUT-RXN

`reaction.ecocyc.PPENTOMUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PPENTOMUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the catabolism of ribo- and deoxyribonucleosides. EcoCyc reaction equation: RIBOSE-1P -> RIBOSE-5P; direction=REVERSIBLE. This reaction is involved in the catabolism of ribo- and deoxyribonucleosides.

## Biological Role

Catalyzed by deoB (protein.P0A6K6). Substrates: alpha-D-Ribose 1-phosphate (molecule.C00620). Products: D-Ribose 5-phosphate (molecule.C00117).

## Enriched Pathways

- `ecocyc.PWY0-1295` pyrimidine ribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)

## Annotation

This reaction is involved in the catabolism of ribo- and deoxyribonucleosides.

## Pathways

- `ecocyc.PWY0-1295` pyrimidine ribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A6K6|protein.P0A6K6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PPENTOMUT-RXN`

## Notes

RIBOSE-1P -> RIBOSE-5P; direction=REVERSIBLE
