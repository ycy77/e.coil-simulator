---
entity_id: "reaction.ecocyc.RXN-14023"
entity_type: "reaction"
name: "RXN-14023"
source_database: "EcoCyc"
source_id: "RXN-14023"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14023

`reaction.ecocyc.RXN-14023`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14023`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCOL + NAD -> GLYCOLALDEHYDE + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: GLYCOL + NAD -> GLYCOLALDEHYDE + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by NADPH-dependent aldehyde reductase YqhD (complex.ecocyc.CPLX0-7667). Substrates: NAD+ (molecule.C00003), Ethylene glycol (molecule.C01380). Products: NADH (molecule.C00004), H+ (molecule.C00080), Glycolaldehyde (molecule.C00266).

## Annotation

GLYCOL + NAD -> GLYCOLALDEHYDE + NADH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7667|complex.ecocyc.CPLX0-7667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01380|molecule.C01380]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14023`

## Notes

GLYCOL + NAD -> GLYCOLALDEHYDE + NADH + PROTON; direction=REVERSIBLE
