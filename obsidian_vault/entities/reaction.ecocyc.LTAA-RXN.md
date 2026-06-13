---
entity_id: "reaction.ecocyc.LTAA-RXN"
entity_type: "reaction"
name: "LTAA-RXN"
source_database: "EcoCyc"
source_id: "LTAA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LTAA-RXN

`reaction.ecocyc.LTAA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LTAA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ALLO-THREONINE -> GLY + ACETALD; direction=REVERSIBLE EcoCyc reaction equation: L-ALLO-THREONINE -> GLY + ACETALD; direction=REVERSIBLE.

## Biological Role

Catalyzed by low-specificity L-threonine aldolase (complex.ecocyc.LTAA-CPLX). Substrates: L-Allothreonine (molecule.C05519). Products: Glycine (molecule.C00037), Acetaldehyde (molecule.C00084).

## Annotation

L-ALLO-THREONINE -> GLY + ACETALD; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.LTAA-CPLX|complex.ecocyc.LTAA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05519|molecule.C05519]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LTAA-RXN`

## Notes

L-ALLO-THREONINE -> GLY + ACETALD; direction=REVERSIBLE
