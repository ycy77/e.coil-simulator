---
entity_id: "reaction.ecocyc.TRANS-RXN0-532"
entity_type: "reaction"
name: "glycine betaine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-532"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glycine betaine:proton antiport

`reaction.ecocyc.TRANS-RXN0-532`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-532`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

BETAINE + PROTON -> BETAINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: BETAINE + PROTON -> BETAINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by multidrug efflux pump EmrE / betaine:H+ antiporter (complex.ecocyc.CPLX0-7963). Substrates: H+ (molecule.C00080), Betaine (molecule.C00719). Products: H+ (molecule.C00080), Betaine (molecule.C00719).

## Annotation

BETAINE + PROTON -> BETAINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-532`

## Notes

BETAINE + PROTON -> BETAINE + PROTON; direction=REVERSIBLE
