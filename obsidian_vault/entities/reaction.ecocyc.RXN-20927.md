---
entity_id: "reaction.ecocyc.RXN-20927"
entity_type: "reaction"
name: "RXN-20927"
source_database: "EcoCyc"
source_id: "RXN-20927"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20927

`reaction.ecocyc.RXN-20927`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20927`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Deoxy-Ribonucleoside-Triphosphates + DNA-N -> DNA-N + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Deoxy-Ribonucleoside-Triphosphates + DNA-N -> DNA-N + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dinB (protein.Q47155). Substrates: a 2'-deoxyribonucleoside 5'-triphosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

Deoxy-Ribonucleoside-Triphosphates + DNA-N -> DNA-N + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.Q47155|protein.Q47155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20927`

## Notes

Deoxy-Ribonucleoside-Triphosphates + DNA-N -> DNA-N + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
