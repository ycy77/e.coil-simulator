---
entity_id: "reaction.ecocyc.RXN0-5240"
entity_type: "reaction"
name: "RXN0-5240"
source_database: "EcoCyc"
source_id: "RXN0-5240"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5240

`reaction.ecocyc.RXN0-5240`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5240`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-ALANINE + PYRIDOXAL_PHOSPHATE -> PYRUVATE + PYRIDOXAMINE-5P; direction=REVERSIBLE EcoCyc reaction equation: D-ALANINE + PYRIDOXAL_PHOSPHATE -> PYRUVATE + PYRIDOXAMINE-5P; direction=REVERSIBLE.

## Biological Role

Catalyzed by serine hydroxymethyltransferase (complex.ecocyc.GLYOHMETRANS-CPLX). Substrates: Pyridoxal phosphate (molecule.C00018), D-Alanine (molecule.C00133). Products: Pyruvate (molecule.C00022), Pyridoxamine phosphate (molecule.C00647).

## Annotation

D-ALANINE + PYRIDOXAL_PHOSPHATE -> PYRUVATE + PYRIDOXAMINE-5P; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.GLYOHMETRANS-CPLX|complex.ecocyc.GLYOHMETRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00647|molecule.C00647]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5240`

## Notes

D-ALANINE + PYRIDOXAL_PHOSPHATE -> PYRUVATE + PYRIDOXAMINE-5P; direction=REVERSIBLE
