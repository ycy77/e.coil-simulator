---
entity_id: "reaction.ecocyc.RXN-11811"
entity_type: "reaction"
name: "RXN-11811"
source_database: "EcoCyc"
source_id: "RXN-11811"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-EXTRACELLULAR|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11811

`reaction.ecocyc.RXN-11811`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11811`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-EXTRACELLULAR|CCO-PERI-BAC

## Enriched Summary

AMMONIA + PROTON -> AMMONIUM; direction=REVERSIBLE EcoCyc reaction equation: AMMONIA + PROTON -> AMMONIUM; direction=REVERSIBLE.

## Biological Role

Substrates: Ammonia (molecule.C00014), H+ (molecule.C00080). Products: ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

AMMONIA + PROTON -> AMMONIUM; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11811`

## Notes

AMMONIA + PROTON -> AMMONIUM; direction=REVERSIBLE
