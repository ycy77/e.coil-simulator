---
entity_id: "reaction.ecocyc.RXN-9628"
entity_type: "reaction"
name: "RXN-9628"
source_database: "EcoCyc"
source_id: "RXN-9628"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9628

`reaction.ecocyc.RXN-9628`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9628`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10267 + WATER -> PROTON + CPD-3617 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10267 + WATER -> PROTON + CPD-3617 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yigI (protein.P0ADP2). Substrates: H2O (molecule.C00001), Decanoyl-CoA (molecule.C05274). Products: CoA (molecule.C00010), H+ (molecule.C00080), Decanoic acid (molecule.C01571).

## Annotation

CPD-10267 + WATER -> PROTON + CPD-3617 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ADP2|protein.P0ADP2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01571|molecule.C01571]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05274|molecule.C05274]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9628`

## Notes

CPD-10267 + WATER -> PROTON + CPD-3617 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
