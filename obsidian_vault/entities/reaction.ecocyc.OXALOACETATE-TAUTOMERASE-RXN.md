---
entity_id: "reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN"
entity_type: "reaction"
name: "OXALOACETATE-TAUTOMERASE-RXN"
source_database: "EcoCyc"
source_id: "OXALOACETATE-TAUTOMERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OXALOACETATE-TAUTOMERASE-RXN

`reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OXALOACETATE-TAUTOMERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OXALACETIC_ACID -> ENOL-OXALOACETATE; direction=REVERSIBLE EcoCyc reaction equation: OXALACETIC_ACID -> ENOL-OXALOACETATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by fumarase A (complex.ecocyc.FUMARASE-A), ycgM (protein.P76004). Substrates: Oxaloacetate (molecule.C00036). Products: 2-Hydroxyethylenedicarboxylate (molecule.C03981).

## Annotation

OXALACETIC_ACID -> ENOL-OXALOACETATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.FUMARASE-A|complex.ecocyc.FUMARASE-A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76004|protein.P76004]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03981|molecule.C03981]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:OXALOACETATE-TAUTOMERASE-RXN`

## Notes

OXALACETIC_ACID -> ENOL-OXALOACETATE; direction=REVERSIBLE
