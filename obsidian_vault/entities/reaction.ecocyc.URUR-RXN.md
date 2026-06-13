---
entity_id: "reaction.ecocyc.URUR-RXN"
entity_type: "reaction"
name: "URUR-RXN"
source_database: "EcoCyc"
source_id: "URUR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URUR-RXN

`reaction.ecocyc.URUR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URUR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2298 + WATER -> CPD-1091 + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2298 + WATER -> CPD-1091 + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by allE (protein.P75713). Substrates: H2O (molecule.C00001), (S)-Ureidoglycine (molecule.C02091). Products: (S)-Ureidoglycolate (molecule.C00603), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Annotation

CPD0-2298 + WATER -> CPD-1091 + AMMONIUM; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75713|protein.P75713]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00603|molecule.C00603]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02091|molecule.C02091]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:URUR-RXN`

## Notes

CPD0-2298 + WATER -> CPD-1091 + AMMONIUM; direction=LEFT-TO-RIGHT
