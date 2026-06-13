---
entity_id: "reaction.ecocyc.RXN0-280"
entity_type: "reaction"
name: "RXN0-280"
source_database: "EcoCyc"
source_id: "RXN0-280"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-280

`reaction.ecocyc.RXN0-280`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-280`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Alkanesulfonates + OXYGEN-MOLECULE + FMNH2 -> Aldehydes + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Alkanesulfonates + OXYGEN-MOLECULE + FMNH2 -> Aldehydes + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by FMNH2-dependent alkanesulfonate monooxygenase (complex.ecocyc.CPLX0-225). Substrates: Oxygen (molecule.C00007), Reduced FMN (molecule.C01847), Alkanesulfonate (molecule.C15521). Products: H2O (molecule.C00001), FMN (molecule.C00061), Aldehyde (molecule.C00071), H+ (molecule.C00080), Sulfite (molecule.C00094).

## Enriched Pathways

- `ecocyc.ALKANEMONOX-PWY` two-component alkanesulfonate monooxygenase (EcoCyc)

## Annotation

Alkanesulfonates + OXYGEN-MOLECULE + FMNH2 -> Aldehydes + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ALKANEMONOX-PWY` two-component alkanesulfonate monooxygenase (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-225|complex.ecocyc.CPLX0-225]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00071|molecule.C00071]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15521|molecule.C15521]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-280`

## Notes

Alkanesulfonates + OXYGEN-MOLECULE + FMNH2 -> Aldehydes + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
