---
entity_id: "reaction.ecocyc.RXN0-7285"
entity_type: "reaction"
name: "homoserine racemase"
source_database: "EcoCyc"
source_id: "RXN0-7285"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# homoserine racemase

`reaction.ecocyc.RXN0-7285`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7285`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HOMO-SER -> CPD-12255; direction=REVERSIBLE EcoCyc reaction equation: HOMO-SER -> CPD-12255; direction=REVERSIBLE.

## Biological Role

Catalyzed by amino acid racemase YgeA (complex.ecocyc.CPLX0-8251). Substrates: L-Homoserine (molecule.C00263). Products: D-homoserine (molecule.ecocyc.CPD-12255).

## Annotation

HOMO-SER -> CPD-12255; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8251|complex.ecocyc.CPLX0-8251]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-12255|molecule.ecocyc.CPD-12255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7285`

## Notes

HOMO-SER -> CPD-12255; direction=REVERSIBLE
