---
entity_id: "reaction.ecocyc.RXN-17918"
entity_type: "reaction"
name: "RXN-17918"
source_database: "EcoCyc"
source_id: "RXN-17918"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17918

`reaction.ecocyc.RXN-17918`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17918`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-Ligase-L-lysine-adenylate + 5-Phospho-terminated-DNAs + PROTON -> A-5-prime-PP-5-prime-DNA + DNA-Ligase-L-lysine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-Ligase-L-lysine-adenylate + 5-Phospho-terminated-DNAs + PROTON -> A-5-prime-PP-5-prime-DNA + DNA-Ligase-L-lysine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a [DNA ligase]-N6-(5'-adenylyl)-L-lysine (molecule.ecocyc.DNA-Ligase-L-lysine-adenylate). Products: a [DNA ligase]-L-lysine (molecule.ecocyc.DNA-Ligase-L-lysine).

## Annotation

DNA-Ligase-L-lysine-adenylate + 5-Phospho-terminated-DNAs + PROTON -> A-5-prime-PP-5-prime-DNA + DNA-Ligase-L-lysine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.DNA-Ligase-L-lysine|molecule.ecocyc.DNA-Ligase-L-lysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-Ligase-L-lysine-adenylate|molecule.ecocyc.DNA-Ligase-L-lysine-adenylate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17918`

## Notes

DNA-Ligase-L-lysine-adenylate + 5-Phospho-terminated-DNAs + PROTON -> A-5-prime-PP-5-prime-DNA + DNA-Ligase-L-lysine; direction=PHYSIOL-LEFT-TO-RIGHT
