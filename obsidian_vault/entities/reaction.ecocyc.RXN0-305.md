---
entity_id: "reaction.ecocyc.RXN0-305"
entity_type: "reaction"
name: "RXN0-305"
source_database: "EcoCyc"
source_id: "RXN0-305"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-305

`reaction.ecocyc.RXN0-305`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-305`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OH-PYR -> TARTRONATE-S-ALD; direction=REVERSIBLE EcoCyc reaction equation: OH-PYR -> TARTRONATE-S-ALD; direction=REVERSIBLE.

## Biological Role

Catalyzed by hydroxypyruvate isomerase (complex.ecocyc.CPLX-171). Substrates: Hydroxypyruvate (molecule.C00168). Products: 2-Hydroxy-3-oxopropanoate (molecule.C01146).

## Annotation

OH-PYR -> TARTRONATE-S-ALD; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX-171|complex.ecocyc.CPLX-171]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01146|molecule.C01146]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00168|molecule.C00168]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-305`

## Notes

OH-PYR -> TARTRONATE-S-ALD; direction=REVERSIBLE
