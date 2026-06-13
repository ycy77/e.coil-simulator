---
entity_id: "reaction.ecocyc.TRANS-RXN0-266"
entity_type: "reaction"
name: "spermidine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-266"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# spermidine:proton antiport

`reaction.ecocyc.TRANS-RXN0-266`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-266`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + SPERMIDINE -> PROTON + SPERMIDINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + SPERMIDINE -> PROTON + SPERMIDINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by multidrug/spermidine efflux pump (complex.ecocyc.YDGEF-CPLX). Substrates: H+ (molecule.C00080), Spermidine (molecule.C00315). Products: H+ (molecule.C00080), Spermidine (molecule.C00315).

## Annotation

PROTON + SPERMIDINE -> PROTON + SPERMIDINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.YDGEF-CPLX|complex.ecocyc.YDGEF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-266`

## Notes

PROTON + SPERMIDINE -> PROTON + SPERMIDINE; direction=REVERSIBLE
