---
entity_id: "reaction.ecocyc.RXN0-7192"
entity_type: "reaction"
name: "RXN0-7192"
source_database: "EcoCyc"
source_id: "RXN0-7192"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7192

`reaction.ecocyc.RXN0-7192`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7192`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BIOTIN + ATP + PROTON -> BIO-5-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: BIOTIN + ATP + PROTON -> BIO-5-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), Biotin (molecule.C00120). Products: Diphosphate (molecule.C00013), Biotinyl-5'-AMP (molecule.C05921).

## Annotation

BIOTIN + ATP + PROTON -> BIO-5-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05921|molecule.C05921]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00120|molecule.C00120]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7192`

## Notes

BIOTIN + ATP + PROTON -> BIO-5-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
