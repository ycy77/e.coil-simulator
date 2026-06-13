---
entity_id: "reaction.ecocyc.TRANS-RXN0-493"
entity_type: "reaction"
name: "sulfadiazine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-493"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# sulfadiazine:proton antiport

`reaction.ecocyc.TRANS-RXN0-493`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-493`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-20940 + PROTON -> PROTON + CPD-20940; direction=REVERSIBLE EcoCyc reaction equation: CPD-20940 + PROTON -> PROTON + CPD-20940; direction=REVERSIBLE.

## Biological Role

Catalyzed by multidrug efflux pump EmrE / betaine:H+ antiporter (complex.ecocyc.CPLX0-7963). Substrates: H+ (molecule.C00080), sulfadiazine (molecule.ecocyc.CPD-20940). Products: H+ (molecule.C00080), sulfadiazine (molecule.ecocyc.CPD-20940).

## Annotation

CPD-20940 + PROTON -> PROTON + CPD-20940; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20940|molecule.ecocyc.CPD-20940]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20940|molecule.ecocyc.CPD-20940]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-493`

## Notes

CPD-20940 + PROTON -> PROTON + CPD-20940; direction=REVERSIBLE
