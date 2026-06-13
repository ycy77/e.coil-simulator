---
entity_id: "reaction.ecocyc.RXN-15999"
entity_type: "reaction"
name: "RXN-15999"
source_database: "EcoCyc"
source_id: "RXN-15999"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15999

`reaction.ecocyc.RXN-15999`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15999`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13430 -> CPD-8938; direction=REVERSIBLE EcoCyc reaction equation: CPD-13430 -> CPD-8938; direction=REVERSIBLE.

## Biological Role

Substrates: 3,6-Anhydro-alpha-L-galactopyranose (molecule.C20902). Products: 3,6-anhydro-L-galactofuranose (molecule.ecocyc.CPD-8938).

## Enriched Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Annotation

CPD-13430 -> CPD-8938; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-8938|molecule.ecocyc.CPD-8938]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20902|molecule.C20902]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15999`

## Notes

CPD-13430 -> CPD-8938; direction=REVERSIBLE
