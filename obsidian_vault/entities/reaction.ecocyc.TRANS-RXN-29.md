---
entity_id: "reaction.ecocyc.TRANS-RXN-29"
entity_type: "reaction"
name: "L-proline:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-29"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-proline:proton symport

`reaction.ecocyc.TRANS-RXN-29`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-29`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + PRO -> PROTON + PRO; direction=REVERSIBLE EcoCyc reaction equation: PROTON + PRO -> PROTON + PRO; direction=REVERSIBLE.

## Biological Role

Catalyzed by osmolyte:H+ symporter ProP (complex.ecocyc.CPLX0-7642). Substrates: H+ (molecule.C00080), L-Proline (molecule.C00148). Products: H+ (molecule.C00080), L-Proline (molecule.C00148).

## Annotation

PROTON + PRO -> PROTON + PRO; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7642|complex.ecocyc.CPLX0-7642]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00213|molecule.C00213]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7082|molecule.ecocyc.CPD-7082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.METHYLNICOTINATE|molecule.ecocyc.METHYLNICOTINATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-29`

## Notes

PROTON + PRO -> PROTON + PRO; direction=REVERSIBLE
