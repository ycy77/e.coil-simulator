---
entity_id: "reaction.ecocyc.RXN0-5101"
entity_type: "reaction"
name: "RXN0-5101"
source_database: "EcoCyc"
source_id: "RXN0-5101"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5101

`reaction.ecocyc.RXN0-5101`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5101`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-903 + NADP -> N-ETHYLMALEIMIDE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD0-903 + NADP -> N-ETHYLMALEIMIDE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by nemA (protein.P77258). Substrates: NADP+ (molecule.C00006), N-ethylsuccinimide (molecule.ecocyc.CPD0-903). Products: NADPH (molecule.C00005), H+ (molecule.C00080), N-ethylmaleimide (molecule.ecocyc.N-ETHYLMALEIMIDE).

## Annotation

CPD0-903 + NADP -> N-ETHYLMALEIMIDE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P77258|protein.P77258]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-903|molecule.ecocyc.CPD0-903]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5101`

## Notes

CPD0-903 + NADP -> N-ETHYLMALEIMIDE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
