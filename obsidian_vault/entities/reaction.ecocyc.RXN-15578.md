---
entity_id: "reaction.ecocyc.RXN-15578"
entity_type: "reaction"
name: "RXN-15578"
source_database: "EcoCyc"
source_id: "RXN-15578"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15578

`reaction.ecocyc.RXN-15578`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15578`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TRP -> INDOLE + 2-AMINOACRYLATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: TRP -> INDOLE + 2-AMINOACRYLATE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Tryptophan (molecule.C00078). Products: Indole (molecule.C00463), Dehydroalanine (molecule.C02218).

## Enriched Pathways

- `ecocyc.TRYPDEG-PWY` L-tryptophan degradation II (via pyruvate) (EcoCyc)

## Annotation

TRP -> INDOLE + 2-AMINOACRYLATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRYPDEG-PWY` L-tryptophan degradation II (via pyruvate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02218|molecule.C02218]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15578`

## Notes

TRP -> INDOLE + 2-AMINOACRYLATE; direction=LEFT-TO-RIGHT
