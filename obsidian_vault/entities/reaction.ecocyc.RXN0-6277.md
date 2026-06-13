---
entity_id: "reaction.ecocyc.RXN0-6277"
entity_type: "reaction"
name: "RXN0-6277"
source_database: "EcoCyc"
source_id: "RXN0-6277"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6277

`reaction.ecocyc.RXN0-6277`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6277`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-722 + Red-Thioredoxin -> BIOTIN + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-722 + Red-Thioredoxin -> BIOTIN + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bisC (protein.P20099). Substrates: Biotin sulfoxide (molecule.C20386). Products: H2O (molecule.C00001), Biotin (molecule.C00120).

## Annotation

CPD-722 + Red-Thioredoxin -> BIOTIN + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P20099|protein.P20099]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00120|molecule.C00120]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20386|molecule.C20386]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.ATABRINE|molecule.ecocyc.ATABRINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1496|molecule.ecocyc.CPD0-1496]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CUSO4|molecule.ecocyc.CUSO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6277`

## Notes

CPD-722 + Red-Thioredoxin -> BIOTIN + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
