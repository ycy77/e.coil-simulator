---
entity_id: "reaction.ecocyc.RXN0-7453"
entity_type: "reaction"
name: "RXN0-7453"
source_database: "EcoCyc"
source_id: "RXN0-7453"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7453

`reaction.ecocyc.RXN0-7453`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7453`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

an-oxidized-SoxR-protein + NADH-P-OR-NOP -> a-reduced-SoxR-protein + NAD-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: an-oxidized-SoxR-protein + NADH-P-OR-NOP -> a-reduced-SoxR-protein + NAD-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by SoxR [2Fe-2S] reducing system (complex.ecocyc.CPLX0-10853). Substrates: NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: H+ (molecule.C00080), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP).

## Annotation

an-oxidized-SoxR-protein + NADH-P-OR-NOP -> a-reduced-SoxR-protein + NAD-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-10853|complex.ecocyc.CPLX0-10853]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7453`

## Notes

an-oxidized-SoxR-protein + NADH-P-OR-NOP -> a-reduced-SoxR-protein + NAD-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT
