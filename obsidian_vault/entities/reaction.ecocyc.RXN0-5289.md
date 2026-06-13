---
entity_id: "reaction.ecocyc.RXN0-5289"
entity_type: "reaction"
name: "RXN0-5289"
source_database: "EcoCyc"
source_id: "RXN0-5289"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5289

`reaction.ecocyc.RXN0-5289`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5289`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the metabolism of glycolate, glyoxylate, D-glucarate and D-galactarate. EcoCyc reaction equation: GLYCERATE + NAD -> CPD-26279 + NADH + PROTON; direction=REVERSIBLE. This reaction is involved in the metabolism of glycolate, glyoxylate, D-glucarate and D-galactarate.

## Biological Role

Catalyzed by tartronate semialdehyde reductase 2 (complex.ecocyc.CPLX0-7616). Substrates: NAD+ (molecule.C00003), D-Glycerate (molecule.C00258). Products: NADH (molecule.C00004), H+ (molecule.C00080), (2R)-tartronate semialdehyde (molecule.ecocyc.CPD-26279).

## Annotation

This reaction is involved in the metabolism of glycolate, glyoxylate, D-glucarate and D-galactarate.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7616|complex.ecocyc.CPLX0-7616]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26279|molecule.ecocyc.CPD-26279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5289`

## Notes

GLYCERATE + NAD -> CPD-26279 + NADH + PROTON; direction=REVERSIBLE
