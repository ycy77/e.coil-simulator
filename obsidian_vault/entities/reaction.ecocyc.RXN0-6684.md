---
entity_id: "reaction.ecocyc.RXN0-6684"
entity_type: "reaction"
name: "RXN0-6684"
source_database: "EcoCyc"
source_id: "RXN0-6684"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6684

`reaction.ecocyc.RXN0-6684`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6684`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRUVATE + AMMONIUM + PROTON + E- -> D-ALANINE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PYRUVATE + AMMONIUM + PROTON + E- -> D-ALANINE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080), ammonium (molecule.ecocyc.AMMONIUM). Products: H2O (molecule.C00001), D-Alanine (molecule.C00133).

## Annotation

PYRUVATE + AMMONIUM + PROTON + E- -> D-ALANINE + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6684`

## Notes

PYRUVATE + AMMONIUM + PROTON + E- -> D-ALANINE + WATER; direction=LEFT-TO-RIGHT
