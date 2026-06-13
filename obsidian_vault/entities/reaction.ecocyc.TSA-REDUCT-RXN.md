---
entity_id: "reaction.ecocyc.TSA-REDUCT-RXN"
entity_type: "reaction"
name: "TSA-REDUCT-RXN"
source_database: "EcoCyc"
source_id: "TSA-REDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TSA-REDUCT-RXN

`reaction.ecocyc.TSA-REDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TSA-REDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the metabolism of glycolate, glyoxylate, D-glucarate and D-galactarate. EcoCyc reaction equation: NAD-P-OR-NOP + GLYCERATE -> CPD-26279 + NADH-P-OR-NOP + PROTON; direction=RIGHT-TO-LEFT. This reaction is involved in the metabolism of glycolate, glyoxylate, D-glucarate and D-galactarate.

## Biological Role

Catalyzed by garR (protein.P0ABQ2). Substrates: D-Glycerate (molecule.C00258), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), (2R)-tartronate semialdehyde (molecule.ecocyc.CPD-26279), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)
- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)
- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)

## Annotation

This reaction is involved in the metabolism of glycolate, glyoxylate, D-glucarate and D-galactarate.

## Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)
- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)
- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABQ2|protein.P0ABQ2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26279|molecule.ecocyc.CPD-26279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TSA-REDUCT-RXN`

## Notes

NAD-P-OR-NOP + GLYCERATE -> CPD-26279 + NADH-P-OR-NOP + PROTON; direction=RIGHT-TO-LEFT
