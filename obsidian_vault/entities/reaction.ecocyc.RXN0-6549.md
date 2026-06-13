---
entity_id: "reaction.ecocyc.RXN0-6549"
entity_type: "reaction"
name: "RXN0-6549"
source_database: "EcoCyc"
source_id: "RXN0-6549"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6549

`reaction.ecocyc.RXN0-6549`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6549`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BROMOACETATE + GLUTATHIONE -> PROTON + CPD0-2370 + BR-; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: BROMOACETATE + GLUTATHIONE -> PROTON + CPD0-2370 + BR-; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by gstB (protein.P0ACA7). Substrates: Glutathione (molecule.C00051), bromoacetate (molecule.ecocyc.BROMOACETATE). Products: H+ (molecule.C00080), bromide (molecule.ecocyc.BR-), S-(acet-2-yl)-glutathione (molecule.ecocyc.CPD0-2370).

## Annotation

BROMOACETATE + GLUTATHIONE -> PROTON + CPD0-2370 + BR-; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ACA7|protein.P0ACA7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.BR-|molecule.ecocyc.BR-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2370|molecule.ecocyc.CPD0-2370]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.BROMOACETATE|molecule.ecocyc.BROMOACETATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6549`

## Notes

BROMOACETATE + GLUTATHIONE -> PROTON + CPD0-2370 + BR-; direction=PHYSIOL-LEFT-TO-RIGHT
