---
entity_id: "reaction.ecocyc.RXN-8668"
entity_type: "reaction"
name: "RXN-8668"
source_database: "EcoCyc"
source_id: "RXN-8668"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8668

`reaction.ecocyc.RXN-8668`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8668`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-S-S-oxides + Red-Thioredoxin; direction=RIGHT-TO-LEFT EcoCyc reaction equation: Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-S-S-oxides + Red-Thioredoxin; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by msrA (protein.P0A744). Substrates: H2O (molecule.C00001), a [protein]-L-methionine (molecule.ecocyc.Protein-L-methionine). Products: a protein-L-methionine-(S)-S-oxide (molecule.ecocyc.Protein-L-methionine-S-S-oxides).

## Annotation

Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-S-S-oxides + Red-Thioredoxin; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A744|protein.P0A744]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Protein-L-methionine-S-S-oxides|molecule.ecocyc.Protein-L-methionine-S-S-oxides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-methionine|molecule.ecocyc.Protein-L-methionine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8668`

## Notes

Protein-L-methionine + Ox-Thioredoxin + WATER -> Protein-L-methionine-S-S-oxides + Red-Thioredoxin; direction=RIGHT-TO-LEFT
