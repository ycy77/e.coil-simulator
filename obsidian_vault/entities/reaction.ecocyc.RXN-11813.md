---
entity_id: "reaction.ecocyc.RXN-11813"
entity_type: "reaction"
name: "RXN-11813"
source_database: "EcoCyc"
source_id: "RXN-11813"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11813

`reaction.ecocyc.RXN-11813`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11813`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12792 + HYDROGEN-PEROXIDE -> PHTHALATE + CPD-13992 + CPD-13993 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12792 + HYDROGEN-PEROXIDE -> PHTHALATE + CPD-13992 + CPD-13993 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yfeX (protein.P76536). Substrates: Hydrogen peroxide (molecule.C00027), Reactive blue 5 (molecule.ecocyc.CPD-12792). Products: H2O (molecule.C00001), H+ (molecule.C00080), Phthalate (molecule.C01606), 2,2'-disulfonyl azobenzene (molecule.ecocyc.CPD-13992), 3-[(4-amino-6-chloro-1,3,5-triazin-2-yl)amino]benzenesulfonate (molecule.ecocyc.CPD-13993).

## Annotation

CPD-12792 + HYDROGEN-PEROXIDE -> PHTHALATE + CPD-13992 + CPD-13993 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P76536|protein.P76536]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01606|molecule.C01606]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13992|molecule.ecocyc.CPD-13992]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13993|molecule.ecocyc.CPD-13993]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12792|molecule.ecocyc.CPD-12792]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11813`

## Notes

CPD-12792 + HYDROGEN-PEROXIDE -> PHTHALATE + CPD-13992 + CPD-13993 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
