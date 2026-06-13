---
entity_id: "reaction.ecocyc.RXN-12440"
entity_type: "reaction"
name: "RXN-12440"
source_database: "EcoCyc"
source_id: "RXN-12440"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12440

`reaction.ecocyc.RXN-12440`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12440`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ASCORBATE + HYDROGEN-PEROXIDE -> ASCORBATE + L-DEHYDRO-ASCORBATE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ASCORBATE + HYDROGEN-PEROXIDE -> ASCORBATE + L-DEHYDRO-ASCORBATE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), Ascorbate (molecule.C00072). Products: H2O (molecule.C00001), Ascorbate (molecule.C00072), Dehydroascorbate (molecule.C05422).

## Enriched Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Annotation

ASCORBATE + HYDROGEN-PEROXIDE -> ASCORBATE + L-DEHYDRO-ASCORBATE + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05422|molecule.C05422]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12440`

## Notes

ASCORBATE + HYDROGEN-PEROXIDE -> ASCORBATE + L-DEHYDRO-ASCORBATE + WATER; direction=LEFT-TO-RIGHT
