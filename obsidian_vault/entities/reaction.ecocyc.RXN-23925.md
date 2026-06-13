---
entity_id: "reaction.ecocyc.RXN-23925"
entity_type: "reaction"
name: "RXN-23925"
source_database: "EcoCyc"
source_id: "RXN-23925"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23925

`reaction.ecocyc.RXN-23925`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23925`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HOMO-SER + ATP + PROTON -> CPD-26478 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HOMO-SER + ATP + PROTON -> CPD-26478 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Homoserine (molecule.C00263). Products: Diphosphate (molecule.C00013), (L-homoseryl)adenylate (molecule.ecocyc.CPD-26478).

## Annotation

HOMO-SER + ATP + PROTON -> CPD-26478 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26478|molecule.ecocyc.CPD-26478]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23925`

## Notes

HOMO-SER + ATP + PROTON -> CPD-26478 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
