---
entity_id: "reaction.ecocyc.RXN-21104"
entity_type: "reaction"
name: "RXN-21104"
source_database: "EcoCyc"
source_id: "RXN-21104"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21104

`reaction.ecocyc.RXN-21104`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21104`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ASN + ATP + PROTON -> CPD-22724 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ASN + ATP + PROTON -> CPD-22724 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Asparagine (molecule.C00152). Products: Diphosphate (molecule.C00013), (L-asparaginyl)adenylate (molecule.ecocyc.CPD-22724).

## Annotation

ASN + ATP + PROTON -> CPD-22724 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22724|molecule.ecocyc.CPD-22724]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21104`

## Notes

ASN + ATP + PROTON -> CPD-22724 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
