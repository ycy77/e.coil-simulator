---
entity_id: "reaction.ecocyc.RXN-24132"
entity_type: "reaction"
name: "hypothiocyanous acid reductase"
source_database: "EcoCyc"
source_id: "RXN-24132"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hypothiocyanous acid reductase

`reaction.ecocyc.RXN-24132`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24132`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-26678 + NADH-P-OR-NOP -> HSCN + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-26678 + NADH-P-OR-NOP -> HSCN + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cupric reductase RclA (complex.ecocyc.CPLX0-8542). Substrates: hypothiocyanous acid (molecule.ecocyc.CPD-26678), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: H2O (molecule.C00001), thiocyanate (molecule.ecocyc.HSCN), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP).

## Annotation

CPD-26678 + NADH-P-OR-NOP -> HSCN + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8542|complex.ecocyc.CPLX0-8542]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.HSCN|molecule.ecocyc.HSCN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26678|molecule.ecocyc.CPD-26678]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24132`

## Notes

CPD-26678 + NADH-P-OR-NOP -> HSCN + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
