---
entity_id: "reaction.ecocyc.TRANS-RXN-369"
entity_type: "reaction"
name: "guanidinium:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-369"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# guanidinium:proton antiport

`reaction.ecocyc.TRANS-RXN-369`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-369`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1470 + PROTON -> CPD0-1470 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1470 + PROTON -> CPD0-1470 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by guanidinium exporter (complex.ecocyc.CPLX0-8263). Substrates: H+ (molecule.C00080), guanidinium (molecule.ecocyc.CPD0-1470). Products: H+ (molecule.C00080), guanidinium (molecule.ecocyc.CPD0-1470).

## Annotation

CPD0-1470 + PROTON -> CPD0-1470 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8263|complex.ecocyc.CPLX0-8263]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1470|molecule.ecocyc.CPD0-1470]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1470|molecule.ecocyc.CPD0-1470]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-20890|molecule.ecocyc.CPD-20890]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-369`

## Notes

CPD0-1470 + PROTON -> CPD0-1470 + PROTON; direction=REVERSIBLE
