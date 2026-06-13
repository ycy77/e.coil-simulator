---
entity_id: "reaction.ecocyc.CHORPYRLY-RXN"
entity_type: "reaction"
name: "CHORPYRLY-RXN"
source_database: "EcoCyc"
source_id: "CHORPYRLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHORPYRLY-RXN

`reaction.ecocyc.CHORPYRLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHORPYRLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in ubiquinone biosynthesis. Ubiquinone is an isoprenoid compound. It functions in electron transport. EcoCyc reaction equation: CHORISMATE -> 4-hydroxybenzoate + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first step in ubiquinone biosynthesis. Ubiquinone is an isoprenoid compound. It functions in electron transport.

## Biological Role

Catalyzed by ubiC (protein.P26602). Substrates: Chorismate (molecule.C00251). Products: Pyruvate (molecule.C00022), 4-Hydroxybenzoate (molecule.C00156).

## Enriched Pathways

- `ecocyc.PWY-5755` 4-hydroxybenzoate biosynthesis II (bacteria) (EcoCyc)

## Annotation

This is the first step in ubiquinone biosynthesis. Ubiquinone is an isoprenoid compound. It functions in electron transport.

## Pathways

- `ecocyc.PWY-5755` 4-hydroxybenzoate biosynthesis II (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P26602|protein.P26602]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00156|molecule.C00156]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00156|molecule.C00156]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00633|molecule.C00633]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06672|molecule.C06672]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-14463|molecule.ecocyc.CPD-14463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CHORPYRLY-RXN`

## Notes

CHORISMATE -> 4-hydroxybenzoate + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
