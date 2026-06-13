---
entity_id: "reaction.ecocyc.TRANS-RXN0-523"
entity_type: "reaction"
name: "D-glycerate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-523"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-glycerate:proton symport

`reaction.ecocyc.TRANS-RXN0-523`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-523`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GLYCERATE + PROTON -> GLYCERATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: GLYCERATE + PROTON -> GLYCERATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by garP (protein.P0AA80), gudP (protein.Q46916). Substrates: H+ (molecule.C00080), D-Glycerate (molecule.C00258). Products: H+ (molecule.C00080), D-Glycerate (molecule.C00258).

## Annotation

GLYCERATE + PROTON -> GLYCERATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AA80|protein.P0AA80]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46916|protein.Q46916]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-523`

## Notes

GLYCERATE + PROTON -> GLYCERATE + PROTON; direction=REVERSIBLE
