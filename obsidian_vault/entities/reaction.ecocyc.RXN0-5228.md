---
entity_id: "reaction.ecocyc.RXN0-5228"
entity_type: "reaction"
name: "RXN0-5228"
source_database: "EcoCyc"
source_id: "RXN0-5228"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5228

`reaction.ecocyc.RXN0-5228`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5228`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2190 -> CPD0-1445; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2190 -> CPD0-1445; direction=REVERSIBLE.

## Biological Role

Catalyzed by ycjG (protein.P51981). Substrates: L-alanyl-D-glutamate (molecule.ecocyc.CPD0-2190). Products: L-alanyl-L-glutamate (molecule.ecocyc.CPD0-1445).

## Enriched Pathways

- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Annotation

CPD0-2190 -> CPD0-1445; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P51981|protein.P51981]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1445|molecule.ecocyc.CPD0-1445]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2190|molecule.ecocyc.CPD0-2190]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5228`

## Notes

CPD0-2190 -> CPD0-1445; direction=REVERSIBLE
