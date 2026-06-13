---
entity_id: "reaction.ecocyc.TRANS-RXN-344"
entity_type: "reaction"
name: "ethidium:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-344"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ethidium:proton antiport

`reaction.ecocyc.TRANS-RXN-344`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-344`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by multidrug efflux pump EmrE / betaine:H+ antiporter (complex.ecocyc.CPLX0-7963). Substrates: H+ (molecule.C00080), ethidium (molecule.ecocyc.CPD0-1938). Products: H+ (molecule.C00080), ethidium (molecule.ecocyc.CPD0-1938).

## Annotation

CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1938|molecule.ecocyc.CPD0-1938]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1938|molecule.ecocyc.CPD0-1938]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-20898|molecule.ecocyc.CPD-20898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-344`

## Notes

CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=REVERSIBLE
