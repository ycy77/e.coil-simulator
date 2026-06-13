---
entity_id: "reaction.ecocyc.RXN-9615"
entity_type: "reaction"
name: "RXN-9615"
source_database: "EcoCyc"
source_id: "RXN-9615"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9615

`reaction.ecocyc.RXN-9615`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9615`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Physiological role is high affinity nitrogen uptake under low nitrogen conditions. EcoCyc reaction equation: AMMONIUM -> AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT. Physiological role is high affinity nitrogen uptake under low nitrogen conditions.

## Biological Role

Catalyzed by ammonium transporter (complex.ecocyc.CPLX0-7532). Substrates: ammonium (molecule.ecocyc.AMMONIUM). Products: ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

Physiological role is high affinity nitrogen uptake under low nitrogen conditions.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7532|complex.ecocyc.CPLX0-7532]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9615`

## Notes

AMMONIUM -> AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
