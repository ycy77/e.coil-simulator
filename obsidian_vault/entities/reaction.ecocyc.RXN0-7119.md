---
entity_id: "reaction.ecocyc.RXN0-7119"
entity_type: "reaction"
name: "RXN0-7119"
source_database: "EcoCyc"
source_id: "RXN0-7119"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7119

`reaction.ecocyc.RXN0-7119`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7119`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ISOBUTANOL + NADP -> CPD-7000 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ISOBUTANOL + NADP -> CPD-7000 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ybbO (protein.P0AFP4), yghA (protein.P0AG84), yahK (protein.P75691), dkgA (protein.Q46857). Substrates: NADP+ (molecule.C00006), isobutanol (molecule.ecocyc.ISOBUTANOL). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2-methylpropanal (molecule.ecocyc.CPD-7000).

## Annotation

ISOBUTANOL + NADP -> CPD-7000 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AFP4|protein.P0AFP4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AG84|protein.P0AG84]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75691|protein.P75691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46857|protein.Q46857]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7000|molecule.ecocyc.CPD-7000]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ISOBUTANOL|molecule.ecocyc.ISOBUTANOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7119`

## Notes

ISOBUTANOL + NADP -> CPD-7000 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
