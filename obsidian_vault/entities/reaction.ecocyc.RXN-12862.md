---
entity_id: "reaction.ecocyc.RXN-12862"
entity_type: "reaction"
name: "RXN-12862"
source_database: "EcoCyc"
source_id: "RXN-12862"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12862

`reaction.ecocyc.RXN-12862`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12862`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-DEHYDRO-ASCORBATE + WATER + PROTON -> CPD-13907; direction=LEFT-TO-RIGHT EcoCyc reaction equation: L-DEHYDRO-ASCORBATE + WATER + PROTON -> CPD-13907; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Dehydroascorbate (molecule.C05422). Products: dehydroascorbate (bicyclic form) (molecule.ecocyc.CPD-13907).

## Annotation

L-DEHYDRO-ASCORBATE + WATER + PROTON -> CPD-13907; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.CPD-13907|molecule.ecocyc.CPD-13907]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05422|molecule.C05422]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12862`

## Notes

L-DEHYDRO-ASCORBATE + WATER + PROTON -> CPD-13907; direction=LEFT-TO-RIGHT
