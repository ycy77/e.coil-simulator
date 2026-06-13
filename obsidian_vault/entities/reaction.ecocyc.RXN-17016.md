---
entity_id: "reaction.ecocyc.RXN-17016"
entity_type: "reaction"
name: "RXN-17016"
source_database: "EcoCyc"
source_id: "RXN-17016"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17016

`reaction.ecocyc.RXN-17016`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17016`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Instance reaction of RXN-10462 required for technical reasons in FBA. EcoCyc reaction equation: Cis-vaccenoyl-ACPs + GLYCEROL-3P -> CPD-18348 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT. Instance reaction of RXN-10462 required for technical reasons in FBA.

## Biological Role

Catalyzed by plsB (protein.P0A7A7). Substrates: sn-Glycerol 3-phosphate (molecule.C00093). Products: 1-cis-vaccenoyl-sn-glycerol-3-phosphate (molecule.ecocyc.CPD-18348).

## Annotation

Instance reaction of RXN-10462 required for technical reasons in FBA.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A7A7|protein.P0A7A7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18348|molecule.ecocyc.CPD-18348]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17016`

## Notes

Cis-vaccenoyl-ACPs + GLYCEROL-3P -> CPD-18348 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
