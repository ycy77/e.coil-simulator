---
entity_id: "reaction.ecocyc.TRANS-RXN0-537"
entity_type: "reaction"
name: "TRANS-RXN0-537"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-537"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-537

`reaction.ecocyc.TRANS-RXN0-537`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-537`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GLY -> GLY; direction=REVERSIBLE EcoCyc reaction equation: GLY -> GLY; direction=REVERSIBLE.

## Biological Role

Catalyzed by glycerol facilitator (complex.ecocyc.CPLX0-7654). Substrates: Glycine (molecule.C00037). Products: Glycine (molecule.C00037).

## Annotation

GLY -> GLY; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-537`

## Notes

GLY -> GLY; direction=REVERSIBLE
