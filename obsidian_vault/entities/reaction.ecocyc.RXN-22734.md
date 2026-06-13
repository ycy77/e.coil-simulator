---
entity_id: "reaction.ecocyc.RXN-22734"
entity_type: "reaction"
name: "RXN-22734"
source_database: "EcoCyc"
source_id: "RXN-22734"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22734

`reaction.ecocyc.RXN-22734`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22734`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-ASPARTATE + AMMONIA -> PPI + AMP + ASN; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + L-ASPARTATE + AMMONIA -> PPI + AMP + ASN; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), L-Aspartate (molecule.C00049). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Asparagine (molecule.C00152).

## Annotation

ATP + L-ASPARTATE + AMMONIA -> PPI + AMP + ASN; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22734`

## Notes

ATP + L-ASPARTATE + AMMONIA -> PPI + AMP + ASN; direction=PHYSIOL-LEFT-TO-RIGHT
