---
entity_id: "reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "QUINATE-5-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "QUINATE-5-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# QUINATE-5-DEHYDROGENASE-RXN

`reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:QUINATE-5-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

QUINATE + NAD-P-OR-NOP -> DEHYDROQUINATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: QUINATE + NAD-P-OR-NOP -> DEHYDROQUINATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by shikimate dehydrogenase / quinate dehydrogenase (complex.ecocyc.CPLX0-7462). Substrates: Quinate (molecule.C00296), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 3-Dehydroquinate (molecule.C00944), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

QUINATE + NAD-P-OR-NOP -> DEHYDROQUINATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7462|complex.ecocyc.CPLX0-7462]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00944|molecule.C00944]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00296|molecule.C00296]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:QUINATE-5-DEHYDROGENASE-RXN`

## Notes

QUINATE + NAD-P-OR-NOP -> DEHYDROQUINATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
