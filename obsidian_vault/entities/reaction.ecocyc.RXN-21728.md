---
entity_id: "reaction.ecocyc.RXN-21728"
entity_type: "reaction"
name: "RXN-21728"
source_database: "EcoCyc"
source_id: "RXN-21728"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21728

`reaction.ecocyc.RXN-21728`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21728`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N7-METHYLGUANINE-IN-DNA + WATER -> DNA-containing-abasic-Sites + CPD0-2377 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N7-METHYLGUANINE-IN-DNA + WATER -> DNA-containing-abasic-Sites + CPD0-2377 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ycaQ (protein.P75843). Substrates: H2O (molecule.C00001), an N7-methylguanine in DNA (molecule.ecocyc.N7-METHYLGUANINE-IN-DNA). Products: H+ (molecule.C00080), N7-methylguanine (molecule.ecocyc.CPD0-2377).

## Annotation

N7-METHYLGUANINE-IN-DNA + WATER -> DNA-containing-abasic-Sites + CPD0-2377 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75843|protein.P75843]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2377|molecule.ecocyc.CPD0-2377]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N7-METHYLGUANINE-IN-DNA|molecule.ecocyc.N7-METHYLGUANINE-IN-DNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21728`

## Notes

N7-METHYLGUANINE-IN-DNA + WATER -> DNA-containing-abasic-Sites + CPD0-2377 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
