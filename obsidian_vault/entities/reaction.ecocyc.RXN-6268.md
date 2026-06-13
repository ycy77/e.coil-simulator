---
entity_id: "reaction.ecocyc.RXN-6268"
entity_type: "reaction"
name: "RXN-6268"
source_database: "EcoCyc"
source_id: "RXN-6268"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-6268

`reaction.ecocyc.RXN-6268`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-6268`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BETAINE-ALDEHYDE-HYDRATE -> BETAINE_ALDEHYDE + WATER; direction=REVERSIBLE EcoCyc reaction equation: BETAINE-ALDEHYDE-HYDRATE -> BETAINE_ALDEHYDE + WATER; direction=REVERSIBLE.

## Biological Role

Substrates: betaine aldehyde hydrate (molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE). Products: H2O (molecule.C00001), Betaine aldehyde (molecule.C00576).

## Annotation

BETAINE-ALDEHYDE-HYDRATE -> BETAINE_ALDEHYDE + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00576|molecule.C00576]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE|molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-6268`

## Notes

BETAINE-ALDEHYDE-HYDRATE -> BETAINE_ALDEHYDE + WATER; direction=REVERSIBLE
