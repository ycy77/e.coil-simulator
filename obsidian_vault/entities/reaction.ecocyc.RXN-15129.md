---
entity_id: "reaction.ecocyc.RXN-15129"
entity_type: "reaction"
name: "RXN-15129"
source_database: "EcoCyc"
source_id: "RXN-15129"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15129

`reaction.ecocyc.RXN-15129`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15129`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS -> 2-AMINOACRYLATE + HS; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CYS -> 2-AMINOACRYLATE + HS; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Cysteine (molecule.C00097). Products: Hydrogen sulfide (molecule.C00283), Dehydroalanine (molecule.C02218).

## Enriched Pathways

- `ecocyc.LCYSDEG-PWY` L-cysteine degradation II (EcoCyc)

## Annotation

CYS -> 2-AMINOACRYLATE + HS; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.LCYSDEG-PWY` L-cysteine degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02218|molecule.C02218]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15129`

## Notes

CYS -> 2-AMINOACRYLATE + HS; direction=LEFT-TO-RIGHT
