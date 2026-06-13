---
entity_id: "reaction.ecocyc.RXN-3523"
entity_type: "reaction"
name: "L-ascorbate:hydrogen-peroxide oxidoreductase"
source_database: "EcoCyc"
source_id: "RXN-3523"
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

`reaction.ecocyc.RXN-3523`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-3523`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-318 -> ASCORBATE + L-DEHYDRO-ASCORBATE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-318 -> ASCORBATE + L-DEHYDRO-ASCORBATE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Monodehydroascorbate (molecule.C01041). Products: Ascorbate (molecule.C00072), H+ (molecule.C00080), Dehydroascorbate (molecule.C05422).

## Annotation

CPD-318 -> ASCORBATE + L-DEHYDRO-ASCORBATE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05422|molecule.C05422]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01041|molecule.C01041]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-3523`

## Notes

CPD-318 -> ASCORBATE + L-DEHYDRO-ASCORBATE + PROTON; direction=LEFT-TO-RIGHT
