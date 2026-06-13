---
entity_id: "reaction.ecocyc.RXN-19775"
entity_type: "reaction"
name: "RXN-19775"
source_database: "EcoCyc"
source_id: "RXN-19775"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19775

`reaction.ecocyc.RXN-19775`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19775`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROQUINONE + HYDROGEN-PEROXIDE -> P-BENZOQUINONE + WATER; direction=REVERSIBLE EcoCyc reaction equation: HYDROQUINONE + HYDROGEN-PEROXIDE -> P-BENZOQUINONE + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by ccp (protein.P37197). Substrates: Hydrogen peroxide (molecule.C00027), Hydroquinone (molecule.C00530). Products: H2O (molecule.C00001), p-Benzoquinone (molecule.C00472).

## Annotation

HYDROQUINONE + HYDROGEN-PEROXIDE -> P-BENZOQUINONE + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37197|protein.P37197]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00472|molecule.C00472]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00530|molecule.C00530]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19775`

## Notes

HYDROQUINONE + HYDROGEN-PEROXIDE -> P-BENZOQUINONE + WATER; direction=REVERSIBLE
