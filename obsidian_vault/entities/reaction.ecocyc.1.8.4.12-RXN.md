---
entity_id: "reaction.ecocyc.1.8.4.12-RXN"
entity_type: "reaction"
name: "1.8.4.12-RXN"
source_database: "EcoCyc"
source_id: "1.8.4.12-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.8.4.12-RXN

`reaction.ecocyc.1.8.4.12-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.8.4.12-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-R-S-oxides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-R-S-oxides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by msrB (protein.P0A746). Substrates: H2O (molecule.C00001), a [protein]-L-methionine (molecule.ecocyc.Protein-L-methionine). Products: a protein-L-methionine-(R)-S-oxide (molecule.ecocyc.Protein-L-methionine-R-S-oxides).

## Annotation

Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-R-S-oxides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A746|protein.P0A746]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Protein-L-methionine-R-S-oxides|molecule.ecocyc.Protein-L-methionine-R-S-oxides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-methionine|molecule.ecocyc.Protein-L-methionine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.8.4.12-RXN`

## Notes

Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-R-S-oxides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT
