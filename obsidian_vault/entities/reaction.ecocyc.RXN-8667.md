---
entity_id: "reaction.ecocyc.RXN-8667"
entity_type: "reaction"
name: "RXN-8667"
source_database: "EcoCyc"
source_id: "RXN-8667"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "KatG"
---

# RXN-8667

`reaction.ecocyc.RXN-8667`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8667`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Donor-H2 + HYDROGEN-PEROXIDE -> Acceptor + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Donor-H2 + HYDROGEN-PEROXIDE -> Acceptor + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by catalase/hydroperoxidase HPI (complex.ecocyc.HYDROPEROXIDI-CPLX). Substrates: Hydrogen peroxide (molecule.C00027). Products: H2O (molecule.C00001).

## Annotation

Donor-H2 + HYDROGEN-PEROXIDE -> Acceptor + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.HYDROPEROXIDI-CPLX|complex.ecocyc.HYDROPEROXIDI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8667`

## Notes

Donor-H2 + HYDROGEN-PEROXIDE -> Acceptor + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
