---
entity_id: "reaction.ecocyc.RXN0-7185"
entity_type: "reaction"
name: "RXN0-7185"
source_database: "EcoCyc"
source_id: "RXN0-7185"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7185

`reaction.ecocyc.RXN0-7185`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7185`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-8990 + WATER + ATP -> CPD-8990 + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8990 + WATER + ATP -> CPD-8990 + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-methionine-(R)-S-oxide (molecule.ecocyc.CPD-8990). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-methionine-(R)-S-oxide (molecule.ecocyc.CPD-8990), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-8990 + WATER + ATP -> CPD-8990 + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8990|molecule.ecocyc.CPD-8990]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8990|molecule.ecocyc.CPD-8990]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7185`

## Notes

CPD-8990 + WATER + ATP -> CPD-8990 + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
