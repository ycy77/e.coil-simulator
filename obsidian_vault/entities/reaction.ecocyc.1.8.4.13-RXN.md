---
entity_id: "reaction.ecocyc.1.8.4.13-RXN"
entity_type: "reaction"
name: "1.8.4.13-RXN"
source_database: "EcoCyc"
source_id: "1.8.4.13-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.8.4.13-RXN

`reaction.ecocyc.1.8.4.13-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.8.4.13-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MET + Ox-Thioredoxin + WATER -> CPD-8989 + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: MET + Ox-Thioredoxin + WATER -> CPD-8989 + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by msrA (protein.P0A744), bisC (protein.P20099). Substrates: H2O (molecule.C00001), L-Methionine (molecule.C00073). Products: L-methionine-(S)-S-oxide (molecule.ecocyc.CPD-8989).

## Annotation

MET + Ox-Thioredoxin + WATER -> CPD-8989 + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A744|protein.P0A744]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P20099|protein.P20099]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-8989|molecule.ecocyc.CPD-8989]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.8.4.13-RXN`

## Notes

MET + Ox-Thioredoxin + WATER -> CPD-8989 + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT
