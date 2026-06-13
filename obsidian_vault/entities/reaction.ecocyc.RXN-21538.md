---
entity_id: "reaction.ecocyc.RXN-21538"
entity_type: "reaction"
name: "RXN-21538"
source_database: "EcoCyc"
source_id: "RXN-21538"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21538

`reaction.ecocyc.RXN-21538`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21538`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

METHIONINE-SYNTHASE-METHYLCOBALAMIN + HOMO-CYS -> Methionine-synthase-cob-I-alamins + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: METHIONINE-SYNTHASE-METHYLCOBALAMIN + HOMO-CYS -> Methionine-synthase-cob-I-alamins + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Homocysteine (molecule.C00155), [Methionine synthase]-methylcob(III)alamin (molecule.C06410). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), cob(I)alamin-[methionine synthase] (molecule.ecocyc.Methionine-synthase-cob-I-alamins).

## Annotation

METHIONINE-SYNTHASE-METHYLCOBALAMIN + HOMO-CYS -> Methionine-synthase-cob-I-alamins + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Methionine-synthase-cob-I-alamins|molecule.ecocyc.Methionine-synthase-cob-I-alamins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06410|molecule.C06410]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21538`

## Notes

METHIONINE-SYNTHASE-METHYLCOBALAMIN + HOMO-CYS -> Methionine-synthase-cob-I-alamins + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
