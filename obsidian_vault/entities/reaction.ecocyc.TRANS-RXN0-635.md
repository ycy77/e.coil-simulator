---
entity_id: "reaction.ecocyc.TRANS-RXN0-635"
entity_type: "reaction"
name: "TRANS-RXN0-635"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-635"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-635

`reaction.ecocyc.TRANS-RXN0-635`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-635`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-20890 + PROTON -> CPD-20890 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20890 + PROTON -> CPD-20890 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump EmrE / betaine:H+ antiporter (complex.ecocyc.CPLX0-7963). Substrates: H+ (molecule.C00080), tetraphenylphosphonium (molecule.ecocyc.CPD-20890). Products: H+ (molecule.C00080), tetraphenylphosphonium (molecule.ecocyc.CPD-20890).

## Annotation

CPD-20890 + PROTON -> CPD-20890 + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20890|molecule.ecocyc.CPD-20890]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20890|molecule.ecocyc.CPD-20890]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-635`

## Notes

CPD-20890 + PROTON -> CPD-20890 + PROTON; direction=LEFT-TO-RIGHT
