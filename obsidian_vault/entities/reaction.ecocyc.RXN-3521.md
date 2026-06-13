---
entity_id: "reaction.ecocyc.RXN-3521"
entity_type: "reaction"
name: "L-ascorbate:hydrogen-peroxide oxidoreductase"
source_database: "EcoCyc"
source_id: "RXN-3521"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "<small>L</small>-ascorbic acid peroxidase"
  - "<small>L</small>-ascorbic acid-specific peroxidase"
  - "ascorbate peroxidase"
  - "ascorbic acid peroxidase"
---

# L-ascorbate:hydrogen-peroxide oxidoreductase

`reaction.ecocyc.RXN-3521`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-3521`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ASCORBATE + HYDROGEN-PEROXIDE + PROTON -> CPD-318 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ASCORBATE + HYDROGEN-PEROXIDE + PROTON -> CPD-318 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), Ascorbate (molecule.C00072), H+ (molecule.C00080). Products: H2O (molecule.C00001), Monodehydroascorbate (molecule.C01041).

## Annotation

ASCORBATE + HYDROGEN-PEROXIDE + PROTON -> CPD-318 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01041|molecule.C01041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-3521`

## Notes

ASCORBATE + HYDROGEN-PEROXIDE + PROTON -> CPD-318 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
