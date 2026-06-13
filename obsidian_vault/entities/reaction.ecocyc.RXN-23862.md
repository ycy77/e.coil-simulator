---
entity_id: "reaction.ecocyc.RXN-23862"
entity_type: "reaction"
name: "5'-exoribonuclease"
source_database: "EcoCyc"
source_id: "RXN-23862"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5'-exoribonuclease

`reaction.ecocyc.RXN-23862`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23862`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Phospho-RNA + WATER -> 5-Phospho-RNA + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-Phospho-RNA + WATER -> 5-Phospho-RNA + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rnm (protein.P77766). Substrates: H2O (molecule.C00001). Products: a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates).

## Annotation

5-Phospho-RNA + WATER -> 5-Phospho-RNA + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P77766|protein.P77766]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23862`

## Notes

5-Phospho-RNA + WATER -> 5-Phospho-RNA + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
