---
entity_id: "reaction.ecocyc.RXN-21261"
entity_type: "reaction"
name: "RXN-21261"
source_database: "EcoCyc"
source_id: "RXN-21261"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21261

`reaction.ecocyc.RXN-21261`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21261`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-uracil-in-DNA-I + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-terminated-DNAs + URACIL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-uracil-in-DNA-I + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-terminated-DNAs + URACIL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nth (protein.P0AB83). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), Uracil (molecule.C00106), a [DNA]-3'-α,β-unsaturated aldehyde (molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde).

## Annotation

a-uracil-in-DNA-I + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-terminated-DNAs + URACIL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AB83|protein.P0AB83]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde|molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21261`

## Notes

a-uracil-in-DNA-I + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-terminated-DNAs + URACIL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
