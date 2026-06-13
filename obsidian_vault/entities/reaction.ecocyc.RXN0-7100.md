---
entity_id: "reaction.ecocyc.RXN0-7100"
entity_type: "reaction"
name: "RXN0-7100"
source_database: "EcoCyc"
source_id: "RXN0-7100"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7100

`reaction.ecocyc.RXN0-7100`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7100`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rpnA (protein.P31667), ralR (protein.P33229). Substrates: H2O (molecule.C00001). Products: a 5'-phosphooligonucleotide (molecule.ecocyc.5-phosphooligonucleotides).

## Annotation

Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P31667|protein.P31667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33229|protein.P33229]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.5-phosphooligonucleotides|molecule.ecocyc.5-phosphooligonucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7100`

## Notes

Double-Stranded-DNAs + WATER -> 5-phosphooligonucleotides; direction=LEFT-TO-RIGHT
