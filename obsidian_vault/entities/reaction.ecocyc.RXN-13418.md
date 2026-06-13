---
entity_id: "reaction.ecocyc.RXN-13418"
entity_type: "reaction"
name: "RXN-13418"
source_database: "EcoCyc"
source_id: "RXN-13418"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13418

`reaction.ecocyc.RXN-13418`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13418`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-3745 + FMNH2 + OXYGEN-MOLECULE -> GLYCOLALDEHYDE + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3745 + FMNH2 + OXYGEN-MOLECULE -> GLYCOLALDEHYDE + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by FMNH2-dependent alkanesulfonate monooxygenase (complex.ecocyc.CPLX0-225). Substrates: Oxygen (molecule.C00007), Reduced FMN (molecule.C01847), 2-Hydroxyethanesulfonate (molecule.C05123). Products: H2O (molecule.C00001), FMN (molecule.C00061), H+ (molecule.C00080), Sulfite (molecule.C00094), Glycolaldehyde (molecule.C00266).

## Annotation

CPD-3745 + FMNH2 + OXYGEN-MOLECULE -> GLYCOLALDEHYDE + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-225|complex.ecocyc.CPLX0-225]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05123|molecule.C05123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13418`

## Notes

CPD-3745 + FMNH2 + OXYGEN-MOLECULE -> GLYCOLALDEHYDE + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
