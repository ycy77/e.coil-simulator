---
entity_id: "reaction.ecocyc.TRANS-RXN-40"
entity_type: "reaction"
name: "L-arabinose:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-40"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-arabinose:proton antiport

`reaction.ecocyc.TRANS-RXN-40`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-40`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

L-ARABINOSE + PROTON -> PROTON + L-ARABINOSE; direction=REVERSIBLE EcoCyc reaction equation: L-ARABINOSE + PROTON -> PROTON + L-ARABINOSE; direction=REVERSIBLE.

## Biological Role

Catalyzed by sotB (protein.P31122). Substrates: H+ (molecule.C00080), L-Arabinose (molecule.C00259). Products: H+ (molecule.C00080), L-Arabinose (molecule.C00259).

## Annotation

L-ARABINOSE + PROTON -> PROTON + L-ARABINOSE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31122|protein.P31122]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-40`

## Notes

L-ARABINOSE + PROTON -> PROTON + L-ARABINOSE; direction=REVERSIBLE
