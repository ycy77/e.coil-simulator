---
entity_id: "reaction.ecocyc.RXN0-5141"
entity_type: "reaction"
name: "RXN0-5141"
source_database: "EcoCyc"
source_id: "RXN0-5141"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5141

`reaction.ecocyc.RXN0-5141`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5141`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-702 + NADP -> CPD-703 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD-702 + NADP -> CPD-703 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by dkgB (protein.P30863). Substrates: NADP+ (molecule.C00006), 4-nitrobenzyl alcohol (molecule.ecocyc.CPD-702). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 4-nitrobenzaldehyde (molecule.ecocyc.CPD-703).

## Annotation

CPD-702 + NADP -> CPD-703 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P30863|protein.P30863]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-703|molecule.ecocyc.CPD-703]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-702|molecule.ecocyc.CPD-702]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5141`

## Notes

CPD-702 + NADP -> CPD-703 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
