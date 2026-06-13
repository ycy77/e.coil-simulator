---
entity_id: "reaction.ecocyc.RXN3O-9786"
entity_type: "reaction"
name: "antimonite:proton antiport"
source_database: "EcoCyc"
source_id: "RXN3O-9786"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# antimonite:proton antiport

`reaction.ecocyc.RXN3O-9786`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN3O-9786`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD0-2039 -> PROTON + CPD0-2039; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD0-2039 -> PROTON + CPD0-2039; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arsenite/antimonite:H+ antiporter (complex.ecocyc.CPLX-7). Substrates: H+ (molecule.C00080), antimonous acid (molecule.ecocyc.CPD0-2039). Products: H+ (molecule.C00080), antimonous acid (molecule.ecocyc.CPD0-2039).

## Annotation

PROTON + CPD0-2039 -> PROTON + CPD0-2039; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-7|complex.ecocyc.CPLX-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2039|molecule.ecocyc.CPD0-2039]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2039|molecule.ecocyc.CPD0-2039]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN3O-9786`

## Notes

PROTON + CPD0-2039 -> PROTON + CPD0-2039; direction=LEFT-TO-RIGHT
