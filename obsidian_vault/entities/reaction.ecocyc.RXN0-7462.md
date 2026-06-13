---
entity_id: "reaction.ecocyc.RXN0-7462"
entity_type: "reaction"
name: "polyadenylation of an RNA fragment"
source_database: "EcoCyc"
source_id: "RXN0-7462"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# polyadenylation of an RNA fragment

`reaction.ecocyc.RXN0-7462`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7462`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-fragment + ATP -> RNA-fragment-w-polyA-tail + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-fragment + ATP -> RNA-fragment-w-polyA-tail + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pcnB (protein.P0ABF1). Substrates: ATP (molecule.C00002). Products: Diphosphate (molecule.C00013).

## Enriched Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Annotation

tRNA-fragment + ATP -> RNA-fragment-w-polyA-tail + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0ABF1|protein.P0ABF1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7462`

## Notes

tRNA-fragment + ATP -> RNA-fragment-w-polyA-tail + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
