---
entity_id: "reaction.ecocyc.TRANS-RXN-10"
entity_type: "reaction"
name: "arabinose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-10"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# arabinose:proton symport

`reaction.ecocyc.TRANS-RXN-10`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-10`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + L-ARABINOSE -> PROTON + L-ARABINOSE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + L-ARABINOSE -> PROTON + L-ARABINOSE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by araE (protein.P0AE24). Substrates: H+ (molecule.C00080), L-Arabinose (molecule.C00259). Products: H+ (molecule.C00080), L-Arabinose (molecule.C00259).

## Annotation

PROTON + L-ARABINOSE -> PROTON + L-ARABINOSE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AE24|protein.P0AE24]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-10`

## Notes

PROTON + L-ARABINOSE -> PROTON + L-ARABINOSE; direction=LEFT-TO-RIGHT
