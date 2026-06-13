---
entity_id: "reaction.ecocyc.RXN-14065"
entity_type: "reaction"
name: "RXN-14065"
source_database: "EcoCyc"
source_id: "RXN-14065"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14065

`reaction.ecocyc.RXN-14065`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14065`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CMP + WATER -> CYTOSINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CMP + WATER -> CYTOSINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), CMP (molecule.C00055). Products: Cytosine (molecule.C00380), D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317).

## Annotation

CMP + WATER -> CYTOSINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00380|molecule.C00380]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14065`

## Notes

CMP + WATER -> CYTOSINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT
