---
entity_id: "reaction.ecocyc.RXN0-2605"
entity_type: "reaction"
name: "RXN0-2605"
source_database: "EcoCyc"
source_id: "RXN0-2605"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2605

`reaction.ecocyc.RXN0-2605`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2605`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by exodeoxyribonuclease V (complex.ecocyc.RECBCD). Substrates: H2O (molecule.C00001). Products: a 5'-phosphooligonucleotide (molecule.ecocyc.5-phosphooligonucleotides).

## Annotation

Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.RECBCD|complex.ecocyc.RECBCD]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.5-phosphooligonucleotides|molecule.ecocyc.5-phosphooligonucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2605`

## Notes

Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT
