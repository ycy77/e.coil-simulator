---
entity_id: "reaction.ecocyc.3.1.21.1-RXN"
entity_type: "reaction"
name: "3.1.21.1-RXN"
source_database: "EcoCyc"
source_id: "3.1.21.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Pancreatic DNase"
  - "Thymonuclease"
---

# 3.1.21.1-RXN

`reaction.ecocyc.3.1.21.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.21.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is the endonucleolytic cleavage of duplex DNA. EcoCyc reaction equation: Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the endonucleolytic cleavage of duplex DNA.

## Biological Role

Catalyzed by endA (protein.P25736). Substrates: H2O (molecule.C00001). Products: a 5'-phosphooligonucleotide (molecule.ecocyc.5-phosphooligonucleotides).

## Annotation

This reaction is the endonucleolytic cleavage of duplex DNA.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P25736|protein.P25736]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.5-phosphooligonucleotides|molecule.ecocyc.5-phosphooligonucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.21.1-RXN`

## Notes

Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=PHYSIOL-LEFT-TO-RIGHT
