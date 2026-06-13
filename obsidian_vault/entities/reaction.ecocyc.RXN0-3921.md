---
entity_id: "reaction.ecocyc.RXN0-3921"
entity_type: "reaction"
name: "RXN0-3921"
source_database: "EcoCyc"
source_id: "RXN0-3921"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3921

`reaction.ecocyc.RXN0-3921`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3921`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GAMMA-GLUTAMYL-PUTRESCINE + WATER + OXYGEN-MOLECULE -> GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + HYDROGEN-PEROXIDE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GAMMA-GLUTAMYL-PUTRESCINE + WATER + OXYGEN-MOLECULE -> GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + HYDROGEN-PEROXIDE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by puuB (protein.P37906). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), gamma-L-Glutamylputrescine (molecule.C15699). Products: Hydrogen peroxide (molecule.C00027), gamma-Glutamyl-gamma-aminobutyraldehyde (molecule.C15700), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Annotation

GAMMA-GLUTAMYL-PUTRESCINE + WATER + OXYGEN-MOLECULE -> GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + HYDROGEN-PEROXIDE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P37906|protein.P37906]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15700|molecule.C15700]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15699|molecule.C15699]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3921`

## Notes

GAMMA-GLUTAMYL-PUTRESCINE + WATER + OXYGEN-MOLECULE -> GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + HYDROGEN-PEROXIDE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
