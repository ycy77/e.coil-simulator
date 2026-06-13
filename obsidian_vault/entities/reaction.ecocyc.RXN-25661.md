---
entity_id: "reaction.ecocyc.RXN-25661"
entity_type: "reaction"
name: "RXN-25661"
source_database: "EcoCyc"
source_id: "RXN-25661"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25661

`reaction.ecocyc.RXN-25661`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25661`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-18334 + AMMONIUM -> CPD-28313; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18334 + AMMONIUM -> CPD-28313; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 2-Carboxy-1,4-naphthoquinone (molecule.C22039), ammonium (molecule.ecocyc.AMMONIUM). Products: 3-amino-2-carboxy-1,4-naphthoquinone (molecule.ecocyc.CPD-28313).

## Annotation

CPD-18334 + AMMONIUM -> CPD-28313; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-28313|molecule.ecocyc.CPD-28313]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C22039|molecule.C22039]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25661`

## Notes

CPD-18334 + AMMONIUM -> CPD-28313; direction=PHYSIOL-LEFT-TO-RIGHT
