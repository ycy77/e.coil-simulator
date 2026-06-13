---
entity_id: "reaction.ecocyc.RXN-23951"
entity_type: "reaction"
name: "RXN-23951"
source_database: "EcoCyc"
source_id: "RXN-23951"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23951

`reaction.ecocyc.RXN-23951`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23951`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + ATP -> Norvalyl-tRNALeu + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + ATP -> Norvalyl-tRNALeu + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by leuS (protein.P07813). Substrates: ATP (molecule.C00002), L-norvaline (molecule.ecocyc.L-2-AMINOPENTANOIC-ACID). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + ATP -> Norvalyl-tRNALeu + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07813|protein.P07813]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-2-AMINOPENTANOIC-ACID|molecule.ecocyc.L-2-AMINOPENTANOIC-ACID]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23951`

## Notes

LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + ATP -> Norvalyl-tRNALeu + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
