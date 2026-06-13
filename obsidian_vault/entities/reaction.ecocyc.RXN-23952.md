---
entity_id: "reaction.ecocyc.RXN-23952"
entity_type: "reaction"
name: "RXN-23952"
source_database: "EcoCyc"
source_id: "RXN-23952"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23952

`reaction.ecocyc.RXN-23952`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23952`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Norvalyl-tRNALeu + WATER -> LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Norvalyl-tRNALeu + WATER -> LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by leuS (protein.P07813). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), L-norvaline (molecule.ecocyc.L-2-AMINOPENTANOIC-ACID).

## Annotation

Norvalyl-tRNALeu + WATER -> LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P07813|protein.P07813]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-2-AMINOPENTANOIC-ACID|molecule.ecocyc.L-2-AMINOPENTANOIC-ACID]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23952`

## Notes

Norvalyl-tRNALeu + WATER -> LEU-tRNAs + L-2-AMINOPENTANOIC-ACID + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
