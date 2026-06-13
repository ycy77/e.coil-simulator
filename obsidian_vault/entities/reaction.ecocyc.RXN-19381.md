---
entity_id: "reaction.ecocyc.RXN-19381"
entity_type: "reaction"
name: "RXN-19381"
source_database: "EcoCyc"
source_id: "RXN-19381"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19381

`reaction.ecocyc.RXN-19381`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19381`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-CYSTEINE -> HS + 2-AMINOACRYLATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-CYSTEINE -> HS + 2-AMINOACRYLATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: D-Cysteine (molecule.C00793). Products: Hydrogen sulfide (molecule.C00283), Dehydroalanine (molecule.C02218).

## Annotation

D-CYSTEINE -> HS + 2-AMINOACRYLATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02218|molecule.C02218]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00793|molecule.C00793]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19381`

## Notes

D-CYSTEINE -> HS + 2-AMINOACRYLATE; direction=PHYSIOL-LEFT-TO-RIGHT
