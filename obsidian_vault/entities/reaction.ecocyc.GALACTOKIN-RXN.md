---
entity_id: "reaction.ecocyc.GALACTOKIN-RXN"
entity_type: "reaction"
name: "GALACTOKIN-RXN"
source_database: "EcoCyc"
source_id: "GALACTOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GALACTOKIN-RXN

`reaction.ecocyc.GALACTOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GALACTOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of galactose, galactoside and glucose catabolism. EcoCyc reaction equation: ALPHA-D-GALACTOSE + ATP -> PROTON + GALACTOSE-1P + ADP; direction=LEFT-TO-RIGHT. Part of galactose, galactoside and glucose catabolism.

## Biological Role

Catalyzed by galK (protein.P0A6T3). Substrates: ATP (molecule.C00002), alpha-D-Galactose (molecule.C00984). Products: ADP (molecule.C00008), H+ (molecule.C00080), alpha-D-Galactose 1-phosphate (molecule.C00446).

## Enriched Pathways

- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)

## Annotation

Part of galactose, galactoside and glucose catabolism.

## Pathways

- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A6T3|protein.P0A6T3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00446|molecule.C00446]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00984|molecule.C00984]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GALACTOKIN-RXN`

## Notes

ALPHA-D-GALACTOSE + ATP -> PROTON + GALACTOSE-1P + ADP; direction=LEFT-TO-RIGHT
