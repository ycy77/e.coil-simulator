---
entity_id: "reaction.ecocyc.TRANS-RXN-242A"
entity_type: "reaction"
name: "L-homoserine lactone:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-242A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-homoserine lactone:proton antiport

`reaction.ecocyc.TRANS-RXN-242A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-242A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-15554 + PROTON -> CPD-15554 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-15554 + PROTON -> CPD-15554 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by rhtB (protein.P0AG34). Substrates: H+ (molecule.C00080), L-homoserine lactone (molecule.ecocyc.CPD-15554). Products: H+ (molecule.C00080), L-homoserine lactone (molecule.ecocyc.CPD-15554).

## Annotation

CPD-15554 + PROTON -> CPD-15554 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AG34|protein.P0AG34]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15554|molecule.ecocyc.CPD-15554]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15554|molecule.ecocyc.CPD-15554]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-242A`

## Notes

CPD-15554 + PROTON -> CPD-15554 + PROTON; direction=REVERSIBLE
