---
entity_id: "reaction.ecocyc.TRANS-RXN0-233"
entity_type: "reaction"
name: "4-hydroxybenzoate:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-233"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4-hydroxybenzoate:proton antiport

`reaction.ecocyc.TRANS-RXN0-233`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-233`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

4-hydroxybenzoate + PROTON -> 4-hydroxybenzoate + PROTON; direction=REVERSIBLE EcoCyc reaction equation: 4-hydroxybenzoate + PROTON -> 4-hydroxybenzoate + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by aromatic carboxylic acid efflux pump (complex.ecocyc.CPLX0-4). Substrates: H+ (molecule.C00080), 4-Hydroxybenzoate (molecule.C00156). Products: H+ (molecule.C00080), 4-Hydroxybenzoate (molecule.C00156).

## Annotation

4-hydroxybenzoate + PROTON -> 4-hydroxybenzoate + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-4|complex.ecocyc.CPLX0-4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00156|molecule.C00156]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00156|molecule.C00156]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-233`

## Notes

4-hydroxybenzoate + PROTON -> 4-hydroxybenzoate + PROTON; direction=REVERSIBLE
