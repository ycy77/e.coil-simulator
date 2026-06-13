---
entity_id: "reaction.ecocyc.RXN-16420"
entity_type: "reaction"
name: "Knallgas reaction"
source_database: "EcoCyc"
source_id: "RXN-16420"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Knallgas reaction

`reaction.ecocyc.RXN-16420`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16420`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Also known as the Knallgas reaction EcoCyc reaction equation: HYDROGEN-MOLECULE + OXYGEN-MOLECULE -> WATER; direction=LEFT-TO-RIGHT. Also known as the Knallgas reaction

## Biological Role

Catalyzed by hydrogenase 1, oxygen tolerant hydrogenase (complex.ecocyc.CPLX0-8167). Substrates: Oxygen (molecule.C00007), Hydrogen (molecule.C00282). Products: H2O (molecule.C00001).

## Annotation

Also known as the Knallgas reaction

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8167|complex.ecocyc.CPLX0-8167]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16420`

## Notes

HYDROGEN-MOLECULE + OXYGEN-MOLECULE -> WATER; direction=LEFT-TO-RIGHT
