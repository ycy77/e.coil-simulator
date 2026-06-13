---
entity_id: "reaction.ecocyc.TRANS-RXN-62B"
entity_type: "reaction"
name: "glycine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-62B"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glycine:proton symport

`reaction.ecocyc.TRANS-RXN-62B`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-62B`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + GLY -> PROTON + GLY; direction=REVERSIBLE EcoCyc reaction equation: PROTON + GLY -> PROTON + GLY; direction=REVERSIBLE.

## Biological Role

Catalyzed by cycA (protein.P0AAE0). Substrates: Glycine (molecule.C00037), H+ (molecule.C00080). Products: Glycine (molecule.C00037), H+ (molecule.C00080).

## Annotation

PROTON + GLY -> PROTON + GLY; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-62B`

## Notes

PROTON + GLY -> PROTON + GLY; direction=REVERSIBLE
