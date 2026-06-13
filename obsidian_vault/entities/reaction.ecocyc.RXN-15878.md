---
entity_id: "reaction.ecocyc.RXN-15878"
entity_type: "reaction"
name: "RXN-15878"
source_database: "EcoCyc"
source_id: "RXN-15878"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15878

`reaction.ecocyc.RXN-15878`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15878`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROXY-METHYL-BUTENYL-DIP + Oxidized-flavodoxins + WATER + PROTON -> 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: HYDROXY-METHYL-BUTENYL-DIP + Oxidized-flavodoxins + WATER + PROTON -> 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ispG (protein.P62620). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate (molecule.C11811). Products: 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate (molecule.C11453).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Annotation

HYDROXY-METHYL-BUTENYL-DIP + Oxidized-flavodoxins + WATER + PROTON -> 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P62620|protein.P62620]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C11453|molecule.C11453]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11811|molecule.C11811]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15878`

## Notes

HYDROXY-METHYL-BUTENYL-DIP + Oxidized-flavodoxins + WATER + PROTON -> 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT
