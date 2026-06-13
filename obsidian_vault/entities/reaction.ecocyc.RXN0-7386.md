---
entity_id: "reaction.ecocyc.RXN0-7386"
entity_type: "reaction"
name: "RXN0-7386"
source_database: "EcoCyc"
source_id: "RXN0-7386"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7386

`reaction.ecocyc.RXN0-7386`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7386`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Quinones + NADH-P-OR-NOP + PROTON -> Reduced-Quinones + NAD-P-OR-NOP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Quinones + NADH-P-OR-NOP + PROTON -> Reduced-Quinones + NAD-P-OR-NOP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NAD(P)H-dependent nitroreductase NfsB (complex.ecocyc.DIHYDROPTERIREDUCT-CPLX). Substrates: H+ (molecule.C00080), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP), a quinone (molecule.ecocyc.Quinones). Products: NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP), a quinol (molecule.ecocyc.Reduced-Quinones).

## Annotation

Quinones + NADH-P-OR-NOP + PROTON -> Reduced-Quinones + NAD-P-OR-NOP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.DIHYDROPTERIREDUCT-CPLX|complex.ecocyc.DIHYDROPTERIREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Reduced-Quinones|molecule.ecocyc.Reduced-Quinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Quinones|molecule.ecocyc.Quinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7386`

## Notes

Quinones + NADH-P-OR-NOP + PROTON -> Reduced-Quinones + NAD-P-OR-NOP; direction=LEFT-TO-RIGHT
