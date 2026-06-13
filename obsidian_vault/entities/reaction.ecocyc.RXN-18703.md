---
entity_id: "reaction.ecocyc.RXN-18703"
entity_type: "reaction"
name: "RXN-18703"
source_database: "EcoCyc"
source_id: "RXN-18703"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18703

`reaction.ecocyc.RXN-18703`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18703`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TUM1-S-sulfanylcysteine + Red-Thioredoxin -> TUM1-L-cysteine + HS + Ox-Thioredoxin; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TUM1-S-sulfanylcysteine + Red-Thioredoxin -> TUM1-L-cysteine + HS + Ox-Thioredoxin; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: a [3-mercaptopyruvate sulfurtransferase]-S-sulfanyl-L-cysteine (molecule.ecocyc.TUM1-S-sulfanylcysteine). Products: Hydrogen sulfide (molecule.C00283), a [3-mercaptopyruvate sulfurtransferase]-L-cysteine (molecule.ecocyc.TUM1-L-cysteine).

## Annotation

TUM1-S-sulfanylcysteine + Red-Thioredoxin -> TUM1-L-cysteine + HS + Ox-Thioredoxin; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TUM1-L-cysteine|molecule.ecocyc.TUM1-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.TUM1-S-sulfanylcysteine|molecule.ecocyc.TUM1-S-sulfanylcysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18703`

## Notes

TUM1-S-sulfanylcysteine + Red-Thioredoxin -> TUM1-L-cysteine + HS + Ox-Thioredoxin; direction=PHYSIOL-LEFT-TO-RIGHT
