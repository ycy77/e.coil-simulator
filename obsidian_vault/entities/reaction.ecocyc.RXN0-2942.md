---
entity_id: "reaction.ecocyc.RXN0-2942"
entity_type: "reaction"
name: "RXN0-2942"
source_database: "EcoCyc"
source_id: "RXN0-2942"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2942

`reaction.ecocyc.RXN0-2942`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2942`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-With-Recognition-Site + WATER -> DNA-Cleaved-Recognition-Site; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-With-Recognition-Site + WATER -> DNA-Cleaved-Recognition-Site; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mcrA (protein.P24200). Substrates: H2O (molecule.C00001), DNA containing a recognition site (molecule.ecocyc.DNA-With-Recognition-Site). Products: DNA cleaved at recognition site (molecule.ecocyc.DNA-Cleaved-Recognition-Site).

## Annotation

DNA-With-Recognition-Site + WATER -> DNA-Cleaved-Recognition-Site; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P24200|protein.P24200]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.DNA-Cleaved-Recognition-Site|molecule.ecocyc.DNA-Cleaved-Recognition-Site]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-With-Recognition-Site|molecule.ecocyc.DNA-With-Recognition-Site]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2942`

## Notes

DNA-With-Recognition-Site + WATER -> DNA-Cleaved-Recognition-Site; direction=PHYSIOL-LEFT-TO-RIGHT
