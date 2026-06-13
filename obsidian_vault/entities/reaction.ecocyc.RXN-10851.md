---
entity_id: "reaction.ecocyc.RXN-10851"
entity_type: "reaction"
name: "RXN-10851"
source_database: "EcoCyc"
source_id: "RXN-10851"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10851

`reaction.ecocyc.RXN-10851`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10851`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-11281 + Donor-H2 -> CPD-11763 + HS + Acceptor; direction=REVERSIBLE EcoCyc reaction equation: CPD-11281 + Donor-H2 -> CPD-11763 + HS + Acceptor; direction=REVERSIBLE.

## Biological Role

Substrates: S-Sulfanylglutathione (molecule.C17267). Products: Hydrogen sulfide (molecule.C00283), bisorganyltrisulfane (molecule.ecocyc.CPD-11763).

## Annotation

CPD-11281 + Donor-H2 -> CPD-11763 + HS + Acceptor; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-11763|molecule.ecocyc.CPD-11763]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C17267|molecule.C17267]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10851`

## Notes

CPD-11281 + Donor-H2 -> CPD-11763 + HS + Acceptor; direction=REVERSIBLE
