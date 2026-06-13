---
entity_id: "reaction.ecocyc.RXN-9310"
entity_type: "reaction"
name: "RXN-9310"
source_database: "EcoCyc"
source_id: "RXN-9310"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9310

`reaction.ecocyc.RXN-9310`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9310`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9924 -> CPD-9923 + PYRUVATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9924 -> CPD-9923 + PYRUVATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by menH (protein.P37355). Substrates: 2-Succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (molecule.C16519). Products: Pyruvate (molecule.C00022), (1R,6R)-6-Hydroxy-2-succinylcyclohexa-2,4-diene-1-carboxylate (molecule.C05817).

## Enriched Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Annotation

CPD-9924 -> CPD-9923 + PYRUVATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P37355|protein.P37355]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05817|molecule.C05817]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16519|molecule.C16519]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9310`

## Notes

CPD-9924 -> CPD-9923 + PYRUVATE; direction=LEFT-TO-RIGHT
