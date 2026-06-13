---
entity_id: "reaction.ecocyc.RXN0-6484"
entity_type: "reaction"
name: "RXN0-6484"
source_database: "EcoCyc"
source_id: "RXN0-6484"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6484

`reaction.ecocyc.RXN0-6484`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6484`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2353 -> tRNAs + Ribonucleoside-Monophosphates; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2353 -> tRNAs + Ribonucleoside-Monophosphates; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ribonuclease T (complex.ecocyc.CPLX0-3602), rnd (protein.P09155). Products: a ribonucleoside 5'-monophosphate (molecule.ecocyc.Ribonucleoside-Monophosphates).

## Annotation

CPD0-2353 -> tRNAs + Ribonucleoside-Monophosphates; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3602|complex.ecocyc.CPLX0-3602]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P09155|protein.P09155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Ribonucleoside-Monophosphates|molecule.ecocyc.Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN0-6484`

## Notes

CPD0-2353 -> tRNAs + Ribonucleoside-Monophosphates; direction=LEFT-TO-RIGHT
