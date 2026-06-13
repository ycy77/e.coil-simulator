---
entity_id: "reaction.ecocyc.TRANS-RXN-29A"
entity_type: "reaction"
name: "glycine betaine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-29A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glycine betaine:proton symport

`reaction.ecocyc.TRANS-RXN-29A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-29A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + BETAINE -> PROTON + BETAINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + BETAINE -> PROTON + BETAINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by osmolyte:H+ symporter ProP (complex.ecocyc.CPLX0-7642). Substrates: H+ (molecule.C00080), Betaine (molecule.C00719). Products: H+ (molecule.C00080), Betaine (molecule.C00719).

## Annotation

PROTON + BETAINE -> PROTON + BETAINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7642|complex.ecocyc.CPLX0-7642]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-29A`

## Notes

PROTON + BETAINE -> PROTON + BETAINE; direction=REVERSIBLE
