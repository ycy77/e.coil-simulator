---
entity_id: "reaction.ecocyc.RXN-11174"
entity_type: "reaction"
name: "RXN-11174"
source_database: "EcoCyc"
source_id: "RXN-11174"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11174

`reaction.ecocyc.RXN-11174`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11174`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SHIKIMATE + NAD-P-OR-NOP -> 3-DEHYDRO-SHIKIMATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SHIKIMATE + NAD-P-OR-NOP -> 3-DEHYDRO-SHIKIMATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by shikimate dehydrogenase / quinate dehydrogenase (complex.ecocyc.CPLX0-7462). Substrates: Shikimate (molecule.C00493), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 3-Dehydroshikimate (molecule.C02637), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

SHIKIMATE + NAD-P-OR-NOP -> 3-DEHYDRO-SHIKIMATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7462|complex.ecocyc.CPLX0-7462]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02637|molecule.C02637]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00493|molecule.C00493]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11174`

## Notes

SHIKIMATE + NAD-P-OR-NOP -> 3-DEHYDRO-SHIKIMATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
