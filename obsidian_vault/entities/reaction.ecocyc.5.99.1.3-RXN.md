---
entity_id: "reaction.ecocyc.5.99.1.3-RXN"
entity_type: "reaction"
name: "5.99.1.3-RXN"
source_database: "EcoCyc"
source_id: "5.99.1.3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DNA gyrase"
  - "Type II DNA topoisomerase"
---

# 5.99.1.3-RXN

`reaction.ecocyc.5.99.1.3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5.99.1.3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the ATP-dependent breakage, passage and rejoining of double-stranded DNA. EcoCyc reaction equation: Double-Stranded-DNAs + ATP -> Negatively-super-coiled-DNAs + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the ATP-dependent breakage, passage and rejoining of double-stranded DNA.

## Biological Role

Catalyzed by DNA gyrase (complex.ecocyc.CPLX0-2425). Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Annotation

This reaction is the ATP-dependent breakage, passage and rejoining of double-stranded DNA.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2425|complex.ecocyc.CPLX0-2425]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-26635|molecule.ecocyc.CPD-26635]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:5.99.1.3-RXN`

## Notes

Double-Stranded-DNAs + ATP -> Negatively-super-coiled-DNAs + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
