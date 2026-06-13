---
entity_id: "reaction.ecocyc.RXN0-7366"
entity_type: "reaction"
name: "RXN0-7366"
source_database: "EcoCyc"
source_id: "RXN0-7366"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7366

`reaction.ecocyc.RXN0-7366`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7366`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A-NM5-ICL + WATER -> A-DNA-WITH-OPPOSING-AP-SITE + CPD-23534; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: A-NM5-ICL + WATER -> A-DNA-WITH-OPPOSING-AP-SITE + CPD-23534; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ycaQ (protein.P75843). Substrates: H2O (molecule.C00001). Products: a mechlorethamine derived bis-guanyl compound (molecule.ecocyc.CPD-23534).

## Annotation

A-NM5-ICL + WATER -> A-DNA-WITH-OPPOSING-AP-SITE + CPD-23534; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P75843|protein.P75843]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-23534|molecule.ecocyc.CPD-23534]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7366`

## Notes

A-NM5-ICL + WATER -> A-DNA-WITH-OPPOSING-AP-SITE + CPD-23534; direction=PHYSIOL-LEFT-TO-RIGHT
