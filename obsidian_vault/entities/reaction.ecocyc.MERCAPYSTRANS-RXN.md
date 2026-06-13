---
entity_id: "reaction.ecocyc.MERCAPYSTRANS-RXN"
entity_type: "reaction"
name: "MERCAPYSTRANS-RXN"
source_database: "EcoCyc"
source_id: "MERCAPYSTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MERCAPYSTRANS-RXN

`reaction.ecocyc.MERCAPYSTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MERCAPYSTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction converts mercaptopyruvate to pyruvate and sulfur. EcoCyc reaction equation: 3-MERCAPTO-PYRUVATE + Red-Thioredoxin -> PYRUVATE + HS + Ox-Thioredoxin; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction converts mercaptopyruvate to pyruvate and sulfur.

## Biological Role

Catalyzed by sseA (protein.P31142). Substrates: Mercaptopyruvate (molecule.C00957). Products: Pyruvate (molecule.C00022), Hydrogen sulfide (molecule.C00283).

## Enriched Pathways

- `ecocyc.PWY-5329` L-cysteine degradation III (EcoCyc)

## Annotation

This reaction converts mercaptopyruvate to pyruvate and sulfur.

## Pathways

- `ecocyc.PWY-5329` L-cysteine degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P31142|protein.P31142]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00957|molecule.C00957]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MERCAPYSTRANS-RXN`

## Notes

3-MERCAPTO-PYRUVATE + Red-Thioredoxin -> PYRUVATE + HS + Ox-Thioredoxin; direction=PHYSIOL-LEFT-TO-RIGHT
