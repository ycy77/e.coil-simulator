---
entity_id: "reaction.ecocyc.RXN-20478"
entity_type: "reaction"
name: "RXN-20478"
source_database: "EcoCyc"
source_id: "RXN-20478"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20478

`reaction.ecocyc.RXN-20478`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20478`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-thymine-glycol-in-DNA + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-DNA + CPD-18012 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-thymine-glycol-in-DNA + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-DNA + CPD-18012 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nth (protein.P0AB83). Substrates: H2O (molecule.C00001), a thymine glycol in DNA (molecule.ecocyc.a-thymine-glycol-in-DNA). Products: H+ (molecule.C00080), a 5'-phospho-[DNA] (molecule.ecocyc.5-Phospho-DNA), thymine glycol (molecule.ecocyc.CPD-18012), a [DNA]-3'-α,β-unsaturated aldehyde (molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde).

## Annotation

a-thymine-glycol-in-DNA + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-DNA + CPD-18012 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AB83|protein.P0AB83]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-Phospho-DNA|molecule.ecocyc.5-Phospho-DNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18012|molecule.ecocyc.CPD-18012]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde|molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.a-thymine-glycol-in-DNA|molecule.ecocyc.a-thymine-glycol-in-DNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20478`

## Notes

a-thymine-glycol-in-DNA + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-DNA + CPD-18012 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
