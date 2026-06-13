---
entity_id: "reaction.ecocyc.RXN-16381"
entity_type: "reaction"
name: "RXN-16381"
source_database: "EcoCyc"
source_id: "RXN-16381"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16381

`reaction.ecocyc.RXN-16381`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16381`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

URIDYLYL-PROTEIN-PII + WATER -> Gln-B + UMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: URIDYLYL-PROTEIN-PII + WATER -> Gln-B + UMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glnD (protein.P27249). Substrates: H2O (molecule.C00001). Products: UMP (molecule.C00105).

## Annotation

URIDYLYL-PROTEIN-PII + WATER -> Gln-B + UMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P27249|protein.P27249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16381`

## Notes

URIDYLYL-PROTEIN-PII + WATER -> Gln-B + UMP; direction=PHYSIOL-LEFT-TO-RIGHT
