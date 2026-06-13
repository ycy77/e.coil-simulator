---
entity_id: "reaction.ecocyc.RXN-17755"
entity_type: "reaction"
name: "melibionate:proton symport"
source_database: "EcoCyc"
source_id: "RXN-17755"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# melibionate:proton symport

`reaction.ecocyc.RXN-17755`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17755`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD-3801 -> PROTON + CPD-3801; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CPD-3801 -> PROTON + CPD-3801; direction=REVERSIBLE.

## Biological Role

Catalyzed by lacY (protein.P02920), melB (protein.P02921). Substrates: H+ (molecule.C00080), melibionate (molecule.ecocyc.CPD-3801). Products: H+ (molecule.C00080), melibionate (molecule.ecocyc.CPD-3801).

## Annotation

PROTON + CPD-3801 -> PROTON + CPD-3801; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P02920|protein.P02920]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3801|molecule.ecocyc.CPD-3801]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3801|molecule.ecocyc.CPD-3801]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17755`

## Notes

PROTON + CPD-3801 -> PROTON + CPD-3801; direction=REVERSIBLE
