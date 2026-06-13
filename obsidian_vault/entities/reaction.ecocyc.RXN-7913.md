---
entity_id: "reaction.ecocyc.RXN-7913"
entity_type: "reaction"
name: "RXN-7913"
source_database: "EcoCyc"
source_id: "RXN-7913"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7913

`reaction.ecocyc.RXN-7913`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7913`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + DCMP -> ADP + DCDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + DCMP -> ADP + DCDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cmk (protein.P0A6I0). Substrates: ATP (molecule.C00002), dCMP (molecule.C00239). Products: ADP (molecule.C00008), dCDP (molecule.C00705).

## Enriched Pathways

- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)

## Annotation

ATP + DCMP -> ADP + DCDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6I0|protein.P0A6I0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00705|molecule.C00705]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00239|molecule.C00239]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7913`

## Notes

ATP + DCMP -> ADP + DCDP; direction=PHYSIOL-LEFT-TO-RIGHT
